from abaqus import *
from abaqusConstants import *
import __main__

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior


def soil_initial_conditions(depth, rho_soil):
    # initial conditions
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#7f ]',), )
    region = regionToolset.Region(cells=cells1)
    mdb.models['3D_MODEL'].GeostaticStress(name='geostatic_field', region=region,
                                           stressMag1=0, vCoord1=0, stressMag2= - depth * rho_soil * 9.81, vCoord2= - depth,
                                           lateralCoeff1=0.5, lateralCoeff2=None)


def fix_base_bc():
    a = mdb.models['3D_MODEL'].rootAssembly
    f1 = a.instances['soil-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#80844400 ]', ), )
    region = a.Set(faces=faces1, name='all_soil_base')
    mdb.models['3D_MODEL'].DisplacementBC(name='fixed_base',
        createStepName='Initial', region=region, u1=SET, u2=SET, u3=SET,
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET,
        distributionType=UNIFORM, fieldName='', localCsys=None)


def fix_sides_bc():
    a = mdb.models['3D_MODEL'].rootAssembly
    f1 = a.instances['soil-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#20201100 ]', ), )
    region = a.Set(faces=faces1, name='soil_sides')
    mdb.models['3D_MODEL'].DisplacementBC(name='fixed_sides',
        createStepName='Initial', region=region, u1=SET, u2=SET, u3=SET,
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET,
        distributionType=UNIFORM, fieldName='', localCsys=None)


def ini_disp(disp):
    a = mdb.models['3D_MODEL'].rootAssembly
    v1 = a.instances['column-1'].vertices
    verts1 = v1.getSequenceFromMask(mask=('[#10 ]', ), )
    region = a.Set(vertices=verts1, name='col_top')
    mdb.models['3D_MODEL'].DisplacementBC(name='ini_disp',
        createStepName='ini_disp', region=region, u1=disp, u2=UNSET, u3=UNSET,
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF,
        distributionType=UNIFORM, fieldName='', localCsys=None)


def gravity():
    # geostatic -> on soil
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#7f ]', ), )
    region = regionToolset.Region(cells=cells1)
    mdb.models['3D_MODEL'].Gravity(name='gravity_geostatic',
        createStepName='geostatic', comp3=-9.81, distributionType=UNIFORM,
        field='', region=region)

    # static -> on column
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['column-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#3 ]', ), )
    region = regionToolset.Region(cells=cells1)
    mdb.models['3D_MODEL'].Gravity(name='gravity_static', createStepName='static',
        comp3=-9.81, distributionType=UNIFORM, field='', region=region)
