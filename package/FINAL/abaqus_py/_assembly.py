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

def assemble_parts(soil_depth, column_depth):
    # create instances
    a = mdb.models['3D_MODEL'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['3D_MODEL'].parts['column']
    a.Instance(name='column-1', part=p, dependent=OFF)
    p = mdb.models['3D_MODEL'].parts['soil']
    a.Instance(name='soil-1', part=p, dependent=OFF)

    # translate column
    a = mdb.models['3D_MODEL'].rootAssembly
    a.translate(instanceList=('column-1', ), vector=(0.0, 0.0, soil_depth - column_depth))

def merge_parts():
    a1 = mdb.models['3D_MODEL'].rootAssembly
    a1.InstanceFromBooleanMerge(name='merged_parts', instances=(
        a1.instances['column-1'], a1.instances['soil-1'], ),
        keepIntersections=ON,
        originalInstances=SUPPRESS, domain=GEOMETRY)

    # create base set
    p = mdb.models['3D_MODEL'].parts['merged_parts']
    f = p.faces
    faces = f.getSequenceFromMask(mask=('[#421110 ]',), )
    p.Set(faces=faces, name='base_set')
