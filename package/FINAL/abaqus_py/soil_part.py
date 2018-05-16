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

def create_part(diameter, depth):
    s1 = mdb.models['3D_MODEL'].ConstrainedSketch(name='__profile__',
                                                 sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(diameter/2, 0.0))
    p = mdb.models['3D_MODEL'].Part(name='soil', dimensionality=THREE_D,
                                   type=DEFORMABLE_BODY)
    p = mdb.models['3D_MODEL'].parts['soil']
    p.BaseSolidExtrude(sketch=s1, depth=depth)
    s1.unsetPrimaryObject()
    p = mdb.models['3D_MODEL'].parts['soil']
    del mdb.models['3D_MODEL'].sketches['__profile__']


def cut_extrude(diameter, thickness, depth):
    p = mdb.models['3D_MODEL'].parts['soil']
    f, e = p.faces, p.edges
    t = p.MakeSketchTransform(sketchPlane=f[1], sketchUpEdge=e[0],
        sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0))
    s = mdb.models['3D_MODEL'].ConstrainedSketch(name='__profile__',
        sheetSize=119.92, gridSpacing=2.99, transform=t)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['3D_MODEL'].parts['soil']

    p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)

    # outter circle
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(diameter/2.0, 0.0))

    # inner circle
    s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(diameter/2.0 - thickness, 0.0))

    # cut
    p = mdb.models['3D_MODEL'].parts['soil']
    f1, e1 = p.faces, p.edges
    p.CutExtrude(sketchPlane=f1[1], sketchUpEdge=e1[0], sketchPlaneSide=SIDE1,
                 sketchOrientation=RIGHT, sketch=s, depth=depth,
                 flipExtrudeDirection=OFF)
    s.unsetPrimaryObject()
    del mdb.models['3D_MODEL'].sketches['__profile__']


def partition_side_infinite(diameter):
    # sketch circular edge
    p = mdb.models['3D_MODEL'].parts['soil']
    p.DatumAxisByPrincipalAxis(principalAxis=ZAXIS)
    p = mdb.models['3D_MODEL'].parts['soil']
    f, e, d1 = p.faces, p.edges, p.datums
    t = p.MakeSketchTransform(sketchPlane=f[5], sketchUpEdge=e[4],
                              sketchPlaneSide=SIDE1, origin=(0.0, 0.0, 20.0))
    s1 = mdb.models['3D_MODEL'].ConstrainedSketch(name='__profile__',
                                                  sheetSize=113.05, gridSpacing=2.82, transform=t)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=SUPERIMPOSE)
    p = mdb.models['3D_MODEL'].parts['soil']
    p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
    s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(diameter/2.0, 0.0))
    p = mdb.models['3D_MODEL'].parts['soil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]',), )
    f1, e1, d2 = p.faces, p.edges, p.datums
    p.PartitionCellBySketch(sketchPlane=f1[5], sketchUpEdge=e1[4],
                            cells=pickedCells, sketch=s1)
    s1.unsetPrimaryObject()
    del mdb.models['3D_MODEL'].sketches['__profile__']

    # extrude in direction of datum axis z
    p = mdb.models['3D_MODEL'].parts['soil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]',), )
    e, d1 = p.edges, p.datums
    pickedEdges = (e[1],)
    p.PartitionCellByExtrudeEdge(line=d1[3], cells=pickedCells, edges=pickedEdges,
                                 sense=REVERSE)

    # partition infinite boundaries in four partitions (needed to sweep in the right direction)
    p = mdb.models['3D_MODEL'].parts['soil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    e1, v1, d1 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlaneNormalToEdge(edge=e1[0], cells=pickedCells,
        point=p.InterestingPoint(edge=e1[0], rule=MIDDLE))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=127.994,
        farPlane=207.454, width=78.2424, height=43.0001, viewOffsetX=-3.38429,
        viewOffsetY=3.81469)
    p = mdb.models['3D_MODEL'].parts['soil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    e, v, d = p.edges, p.vertices, p.datums
    p.PartitionCellByPlaneNormalToEdge(edge=e[11], cells=pickedCells,
        point=p.InterestingPoint(edge=e[11], rule=MIDDLE))
    p = mdb.models['3D_MODEL'].parts['soil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#4 ]', ), )
    e1, v1, d1 = p.edges, p.vertices, p.datums
    p.PartitionCellByPlaneNormalToEdge(edge=e1[22], cells=pickedCells,
        point=p.InterestingPoint(edge=e1[22], rule=MIDDLE))


def partition_bottom(space):
    # create planum where to cut the partition
    p = mdb.models['3D_MODEL'].parts['soil']
    p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=space)

    # partition on the planum
    p = mdb.models['3D_MODEL'].parts['soil']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#10 ]', ), )
    d = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d[9], cells=pickedCells)
