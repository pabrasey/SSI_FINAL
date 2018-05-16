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

def assign_properties(infinite_bottom):
    # column
    # hex meshing
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['column-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#3 ]',), )
    a.setMeshControls(regions=pickedRegions, elemShape=HEX, technique=SWEEP,
                      algorithm=MEDIAL_AXIS)
    # C3D8 elements
    elemType1 = mesh.ElemType(elemCode=C3D8)
    elemType2 = mesh.ElemType(elemCode=C3D6)
    elemType3 = mesh.ElemType(elemCode=C3D4)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['column-1'].cells
    cells = c1.getSequenceFromMask(mask=('[#3 ]',), )
    pickedRegions = (cells,)
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
                                                       elemType3))

    # finite soil
    # hex meshing
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#3 ]', ), )
    a.setMeshControls(regions=pickedRegions, elemShape=HEX, technique=SWEEP, algorithm=MEDIAL_AXIS)
    # C3D8 elements
    elemType1 = mesh.ElemType(elemCode=C3D8)
    elemType2 = mesh.ElemType(elemCode=C3D6)
    elemType3 = mesh.ElemType(elemCode=C3D4)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells = c1.getSequenceFromMask(mask=('[#3 ]', ), )
    pickedRegions =(cells, )
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
        elemType3))


    # soil center
    # create set
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#40 ]',), )
    a.Set(cells=cells1, name='soil_center')
    # sweep
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#40 ]',), )
    a.setMeshControls(regions=pickedRegions, elemShape=HEX, technique=SWEEP,
                      algorithm=MEDIAL_AXIS)
    # C3D8
    elemType1 = mesh.ElemType(elemCode=C3D8R)
    elemType2 = mesh.ElemType(elemCode=C3D6)
    elemType3 = mesh.ElemType(elemCode=C3D4)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells = c1.getSequenceFromMask(mask=('[#40 ]',), )
    pickedRegions = (cells,)
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
                                                       elemType3))


    '''
    if infinite_bottom:
        # sweep meshing
        a = mdb.models['3D_MODEL'].rootAssembly
        c1 = a.instances['soil-1'].cells
        pickedRegions = c1.getSequenceFromMask(mask=('[#1 ]',), )
        a.setMeshControls(regions=pickedRegions, elemShape=HEX, technique=SWEEP,
                          algorithm=ADVANCING_FRONT)
        a = mdb.models['3D_MODEL'].rootAssembly
        c1 = a.instances['soil-1'].cells
        e1 = a.instances['soil-1'].edges
        a.setSweepPath(region=c1[0], edge=e1[6], sense=REVERSE)
        # acoustic elements
        elemType1 = mesh.ElemType(elemCode=AC3D8, elemLibrary=STANDARD)
        elemType2 = mesh.ElemType(elemCode=AC3D6, elemLibrary=STANDARD)
        elemType3 = mesh.ElemType(elemCode=AC3D4, elemLibrary=STANDARD)
        a = mdb.models['3D_MODEL'].rootAssembly
        c1 = a.instances['soil-1'].cells
        cells1 = c1.getSequenceFromMask(mask=('[#1 ]',), )
        pickedRegions = (cells1,)
        a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
                                                           elemType3))
    else:
        # hex meshing
        a = mdb.models['3D_MODEL'].rootAssembly
        c1 = a.instances['soil-1'].cells
        pickedRegions = c1.getSequenceFromMask(mask=('[#1 ]',), )
        a.setMeshControls(regions=pickedRegions, elemShape=HEX, technique=SWEEP, algorithm=MEDIAL_AXIS)
        # C3D elements
        elemType1 = mesh.ElemType(elemCode=C3D8)
        elemType2 = mesh.ElemType(elemCode=C3D6)
        elemType3 = mesh.ElemType(elemCode=C3D4)
        a = mdb.models['3D_MODEL'].rootAssembly
        c1 = a.instances['soil-1'].cells
        cells = c1.getSequenceFromMask(mask=('[#1 ]',), )
        pickedRegions = (cells,)
        a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
                                                           elemType3))
    '''



def infinite_elements(fixed_sides):
    # assign local seed number = 1 (not used now)
    # --> eventually needed in case of larger infinite elements

    # sweep mesh
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#3c ]',), )
    a.setMeshControls(regions=pickedRegions, technique=SWEEP,
                      algorithm=ADVANCING_FRONT)
    # sweep path
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    e1 = a.instances['soil-1'].edges
    a.setSweepPath(region=c1[2], edge=e1[20], sense=FORWARD)
    a = mdb.models['3D_MODEL'].rootAssembly
    c11 = a.instances['soil-1'].cells
    e11 = a.instances['soil-1'].edges
    a.setSweepPath(region=c11[3], edge=e11[30], sense=REVERSE)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    e1 = a.instances['soil-1'].edges
    a.setSweepPath(region=c1[4], edge=e1[30], sense=REVERSE)
    a = mdb.models['3D_MODEL'].rootAssembly
    c11 = a.instances['soil-1'].cells
    e11 = a.instances['soil-1'].edges
    a.setSweepPath(region=c11[5], edge=e11[34], sense=REVERSE)

    if fixed_sides:
        elemType1 = mesh.ElemType(elemCode=C3D20R)
        elemType2 = mesh.ElemType(elemCode=C3D15)
        elemType3 = mesh.ElemType(elemCode=C3D10)
    else:
        # assign acoustic element
        elemType1 = mesh.ElemType(elemCode=AC3D8, elemLibrary=STANDARD)
        elemType2 = mesh.ElemType(elemCode=AC3D6, elemLibrary=STANDARD)
        elemType3 = mesh.ElemType(elemCode=AC3D4, elemLibrary=STANDARD)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#3c ]', ), )
    pickedRegions =(cells1, )
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2,
        elemType3))


def seed(col_size, soil_size, contact_size):
    a = mdb.models['3D_MODEL'].rootAssembly
    partInstances =(a.instances['soil-1'], )
    a.seedPartInstance(regions=partInstances, size=soil_size, deviationFactor=0.1,
        minSizeFactor=0.1)

    # mesh soil vertical
    a = mdb.models['3D_MODEL'].rootAssembly
    e1 = a.instances['soil-1'].edges
    pickedEdges = e1.getSequenceFromMask(mask=('[#24825b40 #21 ]', ), )
    a.seedEdgeBySize(edges=pickedEdges, size=soil_size, deviationFactor=0.1,
        minSizeFactor=0.1, constraint=FINER)
    a = mdb.models['3D_MODEL'].rootAssembly
    e1 = a.instances['soil-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#24825b40 #21 ]', ), )
    a.Set(edges=edges1, name='soil_vertical_edges')

    a = mdb.models['3D_MODEL'].rootAssembly
    partInstances =(a.instances['column-1'], )
    a.seedPartInstance(regions=partInstances, size=col_size, deviationFactor=0.1,
        minSizeFactor=0.1)

    '''
    # local seed for soil edges in contact with column
    a = mdb.models['3D_MODEL'].rootAssembly
    e1 = a.instances['soil-1'].edges
    pickedEdges = e1.getSequenceFromMask(mask=('[#0 #500 ]', ), )
    a.seedEdgeBySize(edges=pickedEdges, size=contact_size, deviationFactor=0.1,
        constraint=FINER)
    '''

def mesh_parts():
    a = mdb.models['3D_MODEL'].rootAssembly
    partInstances = (a.instances['column-1'], a.instances['soil-1'], )
    a.generateMesh(regions=partInstances)
