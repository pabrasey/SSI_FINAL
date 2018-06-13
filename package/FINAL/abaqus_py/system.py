from abaqus import *
from abaqusConstants import *
import visualization

import column_part
import soil_part
import _materials
import sections_profiles
import _steps
import _assembly
import _interactions
import _mesh
import _loads
import _jobs
import output

import json


class NumericalSystem:

    def __init__(self, steel, soil, super_str, foundation, results_dir, analysisname):

        ''' ---------- Variables ---------- '''

        # soil
        #self.pile_soil_space = 20
        #self.soil_depth = foundation.h + self.pile_soil_space
        self.soil_depth = 100
        self.pile_soil_space = self.soil_depth - foundation.h
        self.soil_diameter = 400 #3.0 * super_str.h
        self.infinites_width = 2
        self.infinites_bottom = False
        self.fixed_sides = True
        self.contact_col_soil = True # False -> tie constraints, True -> contact

        # mesh
        self.col_mesh_size = 4
        self.soil_mesh_size = 4
        self.contact_mesh_size = 2 # not used at the moment !

        # frequency analysis
        self.numEigen = 2  # number of eigenvalue to search for
        self.minEigen = 0  # minimal frequency of interest
        self.maxEigen = 50.0  # max

        # modal dynamics
        self.mod_dyn = False
        self.direct_damping_ratio = 0.0

        # software specific
        self.results_dir = results_dir
        self.analysisname = analysisname

        # geometry
        self.col_r_e = super_str.sec.d_e /2

        ''' ---------- Create Abaqus Model ---------- '''

        # create model
        mdb.Model(name='3D_MODEL')

        # create materials
        _materials.create(steel)
        _materials.create_soil(soil)

        # create parts
        # soil
        soil_part.create_part(self.soil_diameter, self.soil_depth)
        soil_part.cut_extrude(super_str.sec.d_e, super_str.sec.t, foundation.h)

        soil_part.partition_side_infinite(self.soil_diameter - 2 * self.infinites_width)
        soil_part.partition_bottom(space=self.pile_soil_space)

        # column
        column_part.create_part(super_str, foundation, super_str.topmass)
        column_part.partition(foundation)


        # create sections and profiles
        sections_profiles.create_column_section()
        sections_profiles.create_soil_section()


        # assign sections
        sections_profiles.assign_section()


        # steps

        if self.mod_dyn: # modal dynamic analysis with geo- statitc steps before
            _steps.mod_dyn(2, 0.01)
            _steps.set_direct_damping(1, 5, self.direct_damping_ratio)
        else:
            _steps.freq_analysis(self.numEigen, self.minEigen, self.maxEigen)


        # assembly
        _assembly.assemble_parts(self.soil_depth, foundation.h)

        # apply interactions
        _interactions.interaction_soil_col(self.contact_col_soil)


        # mesh
        _mesh.assign_properties(self.infinites_bottom) # assign tet elements to finite soil part and column
        _mesh.infinite_elements(self.fixed_sides)
        _mesh.seed(self.col_mesh_size, self.soil_mesh_size, self.contact_mesh_size)
        _mesh.mesh_parts()


        # ic, bc, constraints and loads.py

        _loads.fix_base_bc()
        if self.fixed_sides:
            _loads.fix_sides_bc()
        if self.mod_dyn:
            _loads.soil_initial_conditions(depth=self.soil_depth, rho_soil=soil.rho)
            _loads.ini_disp(super_str.h / 300.0)
            _loads.gravity() # applied separatelly for soil and structure in the related steps


        # job

        self.jobname = 'job_infinite_' + self.analysisname

        _jobs.create_job('3D_MODEL', 'job_acoustic')
        _jobs.modify_input_file(self.jobname) # change AC3D8 to CIN3D8 element type
        _jobs.import_input(self.jobname)
        _jobs.create_job('Infinite_MODEL', self.jobname)


    def run_analysis(self):

        job = mdb.jobs[self.jobname]
        job.submit(consistencyChecking=OFF)
        job.waitForCompletion()


    def output(self):
        job = mdb.jobs[self.jobname]
        job.waitForCompletion()
        odb = output.load_odb(self.jobname)

        analysisbasename = self.results_dir + self.analysisname
        data = {}
        if self.mod_dyn:
            data.update(output.plot_top_disp(odb))
            output.visual_dyn(analysisbasename)
        data.update(output.freq(odb))
        data.update(output.soil_u(odb, self.col_r_e, self.soil_diameter / 2 - self.infinites_width, analysisbasename))

        with open(analysisbasename + ".txt", 'wb') as f: # save results in json file
            json.dump(data, f, indent=4)


        #odb.close(odb, write=TRUE)


    def delete_model(self):
        del mdb.models['3D_MODEL']
