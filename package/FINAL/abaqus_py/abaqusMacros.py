# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def specify_view():
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
    session.viewports['Viewport: 1'].view.setViewpoint(viewVector=(0, -1, 0.5), 
        cameraUpVector=(0, 0, 1))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=204.832, 
        farPlane=376.449, width=103.355, height=62.5746, cameraPosition=(
        181.863, -200.561, 133.203), cameraUpVector=(-0.304889, -0.496057, 
        0.813), cameraTarget=(2.09808e-005, 6.67572e-006, 27.5))
    session.viewports['Viewport: 1'].view.setViewpoint(viewVector=(0, -1, 0.5), 
        cameraUpVector=(0, 0, 1))
    session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
        'Viewport: 1', ))
    session.animationController.play(duration=UNLIMITED)
    session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=OFF, 
        compass=OFF)
    session.writeImageAnimation(
        fileName='C:/Users/braseyp/Dropbox/Civil Engineering/ETH/ETH_Projektarbeit_SSI_2018/Software/FINAL/round_tower/package/FINAL/results/test_avi', 
        format=AVI, canvasObjects=(session.viewports['Viewport: 1'], ))


def export_Avi():
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
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='modal_dynamics')
    session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=OFF, 
        compass=OFF)
    session.writeImageAnimation(
        fileName='C:/Users/braseyp/Dropbox/Civil Engineering/ETH/ETH_Projektarbeit_SSI_2018/Software/FINAL/round_tower/package/FINAL/results/test_avi.avi', 
        format=AVI, canvasObjects=(session.viewports['Viewport: 1'], ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        UNDEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='modal_dynamics')
    session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
        'Viewport: 1', ))
    session.animationController.play(duration=UNLIMITED)
    session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=OFF, 
        compass=OFF)
    session.writeImageAnimation(
        fileName='C:/Users/braseyp/Dropbox/Civil Engineering/ETH/ETH_Projektarbeit_SSI_2018/Software/FINAL/round_tower/package/FINAL/results/test_avi.avi', 
        format=AVI, canvasObjects=(session.viewports['Viewport: 1'], ))
    session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=OFF, 
        compass=OFF, timeScale=1, frameRate=50)
    session.writeImageAnimation(
        fileName='C:/Users/braseyp/Dropbox/Civil Engineering/ETH/ETH_Projektarbeit_SSI_2018/Software/FINAL/round_tower/package/FINAL/results/test_avi.avi', 
        format=AVI, canvasObjects=(session.viewports['Viewport: 1'], ))
    session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=OFF, 
        compass=ON)
    session.writeImageAnimation(
        fileName='C:/Users/braseyp/Dropbox/Civil Engineering/ETH/ETH_Projektarbeit_SSI_2018/Software/FINAL/round_tower/package/FINAL/results/test_avi.avi', 
        format=QUICKTIME, canvasObjects=(session.viewports['Viewport: 1'], ))
    session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=OFF, 
        compass=ON, frameRate=8)
    session.writeImageAnimation(
        fileName='C:/Users/braseyp/Dropbox/Civil Engineering/ETH/ETH_Projektarbeit_SSI_2018/Software/FINAL/round_tower/package/FINAL/results/test_avi.avi', 
        format=AVI, canvasObjects=(session.viewports['Viewport: 1'], ))
    session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=OFF, 
        compass=ON)
    session.writeImageAnimation(
        fileName='C:/Users/braseyp/Dropbox/Civil Engineering/ETH/ETH_Projektarbeit_SSI_2018/Software/FINAL/round_tower/package/FINAL/results/test_avi.avi', 
        format=QUICKTIME, canvasObjects=(session.viewports['Viewport: 1'], ))
def zoom():
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
    session.viewports['Viewport: 1'].view.fitView()
    odb = session.odbs['C:/Users/braseyp/Dropbox/Civil Engineering/ETH/ETH_Projektarbeit_SSI_2018/Software/FINAL/round_tower/package/FINAL/abaqus_wd/job_infinite_2018_5_15--16_27_482000.odb']
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    session.mdbData.summary()
    session.animationController.setValues(animationType=NONE)
    session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
        'Viewport: 1', ))
    session.animationController.play(duration=UNLIMITED)
    session.animationController.setValues(animationType=NONE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=173.447, 
        farPlane=406.35, width=525.758, height=214.859, viewOffsetX=9.69398, 
        viewOffsetY=13.7338)
    session.viewports['Viewport: 1'].view.fitView()


def temp_G():
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
    mdb.models['3D_MODEL'].materials['soil'].elastic.setValues(dependencies=1, 
        noTension=ON, table=((87.0, 1.0, 0.0), (88.0, 1.0, 1.0), (89.0, 1.0, 
        2.0)))


def soil_T():
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
    a = mdb.models['3D_MODEL'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=235.027, 
        farPlane=392.383, width=140.733, height=76.3862, cameraPosition=(
        -145.199, -188.007, -193.705), cameraUpVector=(-0.182672, -0.380249, 
        0.906665), cameraTarget=(-15.3671, 4.31759, 32.166), 
        viewOffsetX=25.9542, viewOffsetY=-7.59472)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=246.843, 
        farPlane=380.567, width=53.243, height=28.8988, viewOffsetX=1.71963, 
        viewOffsetY=-30.1668)
    a = mdb.models['3D_MODEL'].rootAssembly
    f1 = a.instances['soil-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#40422200 ]', ), )
    e1 = a.instances['soil-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#20100000 #80 ]', ), )
    region = a.Set(edges=edges1, faces=faces1, name='all_soil_bottom')
    mdb.models['3D_MODEL'].TemperatureBC(name='BC-3', createStepName='Initial', 
        region=region, distributionType=UNIFORM, fieldName='', magnitude=0.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=240.5, 
        farPlane=386.91, width=121.516, height=65.9558, viewOffsetX=2.35941, 
        viewOffsetY=-35.0703)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=212.011, 
        farPlane=352.482, width=107.122, height=58.1428, cameraPosition=(
        -45.4614, -199.161, 212.334), cameraUpVector=(0.0602942, 0.820806, 
        0.568016), cameraTarget=(-2.38302, 60.1008, 23.1506), 
        viewOffsetX=2.07992, viewOffsetY=-30.916)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=214.02, 
        farPlane=350.473, width=113.421, height=61.5616, viewOffsetX=31.2181, 
        viewOffsetY=-30.026)
    a = mdb.models['3D_MODEL'].rootAssembly
    f1 = a.instances['soil-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#20881040 ]', ), )
    e1 = a.instances['soil-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#80000000 #10 ]', ), )
    region = a.Set(edges=edges1, faces=faces1, name='all_soil_top')
    mdb.models['3D_MODEL'].TemperatureBC(name='top_T', createStepName='Initial', 
        region=region, distributionType=UNIFORM, fieldName='', magnitude=0.0)
    mdb.models['3D_MODEL'].boundaryConditions.changeKey(fromName='BC-3', 
        toName='bottom_T')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ini_disp')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='frequency')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ini_disp')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        step='modal_dynamics')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='frequency')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ini_disp')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    mdb.models['3D_MODEL'].CoupledTempDisplacementStep(name='Step-4', 
        previous='modal_dynamics', deltmx=1.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-4')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p1 = mdb.models['3D_MODEL'].parts['soil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    a = mdb.models['3D_MODEL'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')


def mesh_column():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=227.297, 
        farPlane=407.149, width=168.966, height=94.0822, cameraPosition=(
        -197.033, -113.771, 243.762), cameraUpVector=(0.57938, 0.692318, 
        0.430132), cameraTarget=(4.12772, 0.726357, 31.758), 
        viewOffsetX=-7.57213, viewOffsetY=-6.06154)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['column-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#2 ]', ), )
    a.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)
    elemType1 = mesh.ElemType(elemCode=C3D20R)
    elemType2 = mesh.ElemType(elemCode=C3D15)
    elemType3 = mesh.ElemType(elemCode=C3D10)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['column-1'].cells
    cells = c1.getSequenceFromMask(mask=('[#2 ]', ), )
    pickedRegions =(cells, )
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))
    i1 = mdb.models['3D_MODEL'].rootAssembly.allInstances['soil-1']
    leaf = dgm.LeafFromInstance(instances=(i1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['column-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#3 ]', ), )
    a.setMeshControls(regions=pickedRegions, elemShape=HEX, technique=SWEEP, 
        algorithm=MEDIAL_AXIS)
    elemType1 = mesh.ElemType(elemCode=C3D8R)
    elemType2 = mesh.ElemType(elemCode=C3D6)
    elemType3 = mesh.ElemType(elemCode=C3D4)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['column-1'].cells
    cells = c1.getSequenceFromMask(mask=('[#3 ]', ), )
    pickedRegions =(cells, )
    a.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, 
        elemType3))


def mesh_finite_soil():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=233.696, 
        farPlane=406.913, width=173.723, height=96.731, cameraPosition=(
        -280.891, -114.129, -96.7423), cameraUpVector=(-0.103323, 0.190537, 
        0.976227), cameraTarget=(-9.5024, -6.00175, 18.0523), 
        viewOffsetX=-7.78531, viewOffsetY=-6.2322)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=234.05, 
        farPlane=409.871, width=173.986, height=96.8774, cameraPosition=(
        -257.75, -133.86, 147.049), cameraUpVector=(0.524667, 0.455835, 
        0.718985), cameraTarget=(-0.957848, -3.30747, 22.4094), 
        viewOffsetX=-7.79709, viewOffsetY=-6.24163)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#3 ]', ), )
    a.setMeshControls(regions=pickedRegions, elemShape=TET, technique=FREE)


def mesh_infinites():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=241.318, 
        farPlane=386.672, width=214.229, height=118.199, cameraPosition=(
        -32.2048, 94.5367, 320.201), cameraUpVector=(0.0894254, 0.79768, 
        -0.596415), cameraTarget=(2.68304, -0.381521, 23.0554), 
        viewOffsetX=1.21614, viewOffsetY=0.613647)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=258.095, 
        farPlane=369.894, width=88.4619, height=48.8078, viewOffsetX=56.3625, 
        viewOffsetY=11.0652)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=256.79, 
        farPlane=371.199, width=88.0145, height=48.561, viewOffsetX=26.8169, 
        viewOffsetY=5.57906)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=249.327, 
        farPlane=378.662, width=165.377, height=91.2448, viewOffsetX=64.5108, 
        viewOffsetY=11.1964)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=246.963, 
        farPlane=381.026, width=163.809, height=90.3799, viewOffsetX=18.6856, 
        viewOffsetY=-0.171172)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=246.449, 
        farPlane=381.54, width=191.261, height=105.526, viewOffsetX=59.2791, 
        viewOffsetY=-26.4601)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=243.95, 
        farPlane=384.04, width=189.322, height=104.456, cameraPosition=(
        -31.3759, 96.0669, 319.81), cameraUpVector=(0.109588, 0.797074, 
        -0.593854), cameraTarget=(3.51193, 1.14873, 22.6639), 
        viewOffsetX=58.6779, viewOffsetY=-26.1918)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=284.593, 
        farPlane=419.946, width=220.864, height=121.859, cameraPosition=(
        87.5795, -1.40648, 365.108), cameraUpVector=(-0.381011, 0.874504, 
        -0.300124), cameraTarget=(-3.00701, -24.0763, 65.4375), 
        viewOffsetX=68.4539, viewOffsetY=-30.5555)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=280.98, 
        farPlane=423.559, width=218.06, height=120.312, viewOffsetX=65.085, 
        viewOffsetY=22.8773)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=304.963, 
        farPlane=399.576, width=27.1752, height=14.9936, viewOffsetX=36.8637, 
        viewOffsetY=50.7653)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#3c ]', ), )
    a.deleteMesh(regions=pickedRegions)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#3c ]', ), )
    a.setMeshControls(regions=pickedRegions, technique=SWEEP, 
        algorithm=ADVANCING_FRONT)
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
    a.setSweepPath(region=c11[5], edge=e11[18], sense=REVERSE)


def fix_base():
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
    del mdb.models['3D_MODEL'].boundaryConditions['fixed_base']
    session.viewports['Viewport: 1'].view.setValues(nearPlane=244.595, 
        farPlane=416.081, width=159.352, height=87.6115, cameraPosition=(
        113.103, -211.6, -205.841), cameraUpVector=(-0.72006, -0.494653, 
        0.486654), cameraTarget=(-11.7167, -25.3253, 13.8031), 
        viewOffsetX=6.06486, viewOffsetY=-29.0215)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=240.271, 
        farPlane=420.404, width=196.705, height=108.148, viewOffsetX=-4.29346, 
        viewOffsetY=-25.1243)
    a = mdb.models['3D_MODEL'].rootAssembly
    f1 = a.instances['soil-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#80844400 ]', ), )
    region = a.Set(faces=faces1, name='all_soil_base')
    mdb.models['3D_MODEL'].DisplacementBC(name='fixed_base', 
        createStepName='Initial', region=region, u1=SET, u2=SET, u3=SET, 
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, 
        distributionType=UNIFORM, fieldName='', localCsys=None)


def surfaces():
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
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['soil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#2000000 ]', ), )
    a.Surface(side1Faces=side1Faces1, name='soil_col_out_surf')
    srf1 = mdb.models['3D_MODEL'].rootAssembly.surfaces['soil_col_out_surf']
    leaf = dgm.LeafFromMeshSurfaceSets(surfaceSets=(srf1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['soil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#4000000 ]', ), )
    a.Surface(side1Faces=side1Faces1, name='soil_col_in_surf')
    srf1 = mdb.models['3D_MODEL'].rootAssembly.surfaces['soil_col_in_surf']
    leaf = dgm.LeafFromMeshSurfaceSets(surfaceSets=(srf1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=268.262, 
        farPlane=414.972, width=63.0224, height=34.6497, viewOffsetX=3.38416, 
        viewOffsetY=-6.42226)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=268.425, 
        farPlane=414.774, width=63.0607, height=34.6707, cameraPosition=(
        -9.47226, -300.458, 170.424), cameraUpVector=(0.0360569, 0.724187, 
        0.68866), cameraTarget=(55.8969, -2.88159, 18.7971), 
        viewOffsetX=3.38621, viewOffsetY=-6.42616)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=275.487, 
        farPlane=407.713, width=6.58053, height=3.61797, viewOffsetX=1.88279, 
        viewOffsetY=-8.68659)
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['soil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#8000000 ]', ), )
    a.Surface(side1Faces=side1Faces1, name='soil_col_bottom_surf')
    srf1 = mdb.models['3D_MODEL'].rootAssembly.surfaces['soil_col_bottom_surf']
    leaf = dgm.LeafFromMeshSurfaceSets(surfaceSets=(srf1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=270.154, 
        farPlane=413.046, width=55.6917, height=30.6192, viewOffsetX=15.1685, 
        viewOffsetY=-8.37812)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=269.347, 
        farPlane=413.853, width=55.5252, height=30.5277, viewOffsetX=-25.0814, 
        viewOffsetY=-8.20678)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=270.634, 
        farPlane=412.566, width=42.6872, height=23.4694, viewOffsetX=-29.876, 
        viewOffsetY=-7.95828)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=270.971, 
        farPlane=412.229, width=42.7404, height=23.4986, viewOffsetX=-32.3169, 
        viewOffsetY=-7.44267)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=273.311, 
        farPlane=409.889, width=22.7551, height=12.5107, viewOffsetX=-39.3084, 
        viewOffsetY=-7.27304)
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['column-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]', ), )
    a.Surface(side1Faces=side1Faces1, name='col_soil_out_surf')
    srf1 = mdb.models['3D_MODEL'].rootAssembly.surfaces['col_soil_out_surf']
    leaf = dgm.LeafFromMeshSurfaceSets(surfaceSets=(srf1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.undoLast()
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.redoLast()
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['column-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]', ), )
    a.Surface(side1Faces=side1Faces1, name='col_soil_in_surf')
    srf1 = mdb.models['3D_MODEL'].rootAssembly.surfaces['col_soil_in_surf']
    leaf = dgm.LeafFromMeshSurfaceSets(surfaceSets=(srf1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=274.748, 
        farPlane=408.453, width=12.0742, height=6.6384, viewOffsetX=-42.8025, 
        viewOffsetY=-9.2596)
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['column-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#40 ]', ), )
    a.Surface(side1Faces=side1Faces1, name='col_soil_bottom_surf')
    srf1 = mdb.models['3D_MODEL'].rootAssembly.surfaces['col_soil_bottom_surf']
    leaf = dgm.LeafFromMeshSurfaceSets(surfaceSets=(srf1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)


def assign_soil_sec():
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
    p = mdb.models['3D_MODEL'].parts['soil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#7f ]', ), )
    region = p.Set(cells=cells, name='sdfsad')
    p = mdb.models['3D_MODEL'].parts['soil']
    p.SectionAssignment(region=region, sectionName='soil_section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


