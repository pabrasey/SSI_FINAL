from abaqus import *
from abaqusConstants import *
import __main__

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import _assembly
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

def create_part(super_str, foundation, mass):

    s = mdb.models['3D_MODEL'].ConstrainedSketch(name='__profile__',
                                                sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)

    # outter circle
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(super_str.sec.r_e, 0.0))

    # inner circle
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(super_str.sec.r_i, 0.0))

    p = mdb.models['3D_MODEL'].Part(name='column', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p = mdb.models['3D_MODEL'].parts['column']

    # height
    p.BaseSolidExtrude(sketch=s, depth= super_str.h + foundation.h)
    s.unsetPrimaryObject()
    del mdb.models['3D_MODEL'].sketches['__profile__']

    # mass at the top



def partition(foundation):
    # create datum plane
    p = mdb.models['3D_MODEL'].parts['column']
    p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=foundation.h)

    p = mdb.models['3D_MODEL'].parts['column']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    d = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d[2], cells=pickedCells)

'''

    p = mdb.models['3D_MODEL'].parts['column']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    d = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d[3], cells=pickedCells)
'''
