# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def mesh_soil_vertical():
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
    set1 = mdb.models['3D_MODEL'].rootAssembly.allInstances['column-1'].sets['col_set']
    leaf = dgm.LeafFromSets(sets=(set1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=416.815, 
        farPlane=655.86, width=136.433, height=75.9675, viewOffsetX=6.48013, 
        viewOffsetY=-31.5688)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=418.907, 
        farPlane=632.881, width=137.118, height=76.3489, cameraPosition=(
        -472.708, -47.5887, 239.257), cameraUpVector=(0.669312, 0.0832373, 
        0.738304), cameraTarget=(6.92887, -1.84767, 35.4721), 
        viewOffsetX=6.51266, viewOffsetY=-31.7272)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=393.432, 
        farPlane=631.496, width=128.78, height=71.7058, cameraPosition=(
        -124.169, 477.657, 153.586), cameraUpVector=(-0.0215895, -0.551677, 
        0.833779), cameraTarget=(-2.00815, -17.7356, 38.1116), 
        viewOffsetX=6.1166, viewOffsetY=-29.7978)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=371.447, 
        farPlane=640.666, width=121.584, height=67.6992, cameraPosition=(
        362.864, 347.987, 78.0709), cameraUpVector=(-0.506066, -0.0350375, 
        0.861783), cameraTarget=(-21.7703, -4.56848, 40.2149), 
        viewOffsetX=5.77481, viewOffsetY=-28.1327)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=373.301, 
        farPlane=638.813, width=130.378, height=72.5958, viewOffsetX=7.14049, 
        viewOffsetY=-24.8287)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=376.775, 
        farPlane=630.462, width=131.591, height=73.2715, cameraPosition=(
        453.567, 218.629, 44.8077), cameraUpVector=(-0.421104, 0.104398, 
        0.900984), cameraTarget=(-21.7682, 0.186185, 41.4986), 
        viewOffsetX=7.20695, viewOffsetY=-25.0598)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=375.581, 
        farPlane=631.656, width=136.24, height=75.8598, viewOffsetX=13.598, 
        viewOffsetY=-21.4555)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=373.287, 
        farPlane=643.892, width=135.408, height=75.3965, cameraPosition=(
        377.769, 336.702, 71.0252), cameraUpVector=(-0.434824, -0.0902399, 
        0.895983), cameraTarget=(-16.5589, -5.6462, 39.7997), 
        viewOffsetX=13.5149, viewOffsetY=-21.3245)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=373.019, 
        farPlane=644.159, width=156.328, height=87.0451, viewOffsetX=9.66228, 
        viewOffsetY=-22.1384)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=381.854, 
        farPlane=639.466, width=160.031, height=89.1067, cameraPosition=(
        216.394, 392.785, 258.429), cameraUpVector=(-0.601931, -0.447397, 
        0.661449), cameraTarget=(-19.0746, -15.5776, 31.5677), 
        viewOffsetX=9.89112, viewOffsetY=-22.6627)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=387.727, 
        farPlane=633.592, width=125.436, height=69.8443, viewOffsetX=2.38872, 
        viewOffsetY=-20.6289)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=409.613, 
        farPlane=608.116, width=132.517, height=73.7869, cameraPosition=(
        379.656, 44.8134, 349.546), cameraUpVector=(-0.760376, -0.427095, 
        0.489304), cameraTarget=(-25.8746, -14.053, 24.352), 
        viewOffsetX=2.52356, viewOffsetY=-21.7933)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=403.805, 
        farPlane=613.924, width=189.999, height=105.793, viewOffsetX=-41.4131, 
        viewOffsetY=-6.57812)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=401.083, 
        farPlane=616.647, width=188.718, height=105.08, viewOffsetX=11.2585, 
        viewOffsetY=-25.0979)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=409.58, 
        farPlane=608.15, width=141.488, height=78.7822, viewOffsetX=23.3932, 
        viewOffsetY=-33.5428)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=429.861, 
        farPlane=642.333, width=148.494, height=82.6833, cameraPosition=(
        46.8502, 476.308, 256.627), cameraUpVector=(-0.354834, -0.633963, 
        0.687156), cameraTarget=(8.98039, -2.43367, 49.1574), 
        viewOffsetX=24.5516, viewOffsetY=-35.2038)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        activeCutName='Y-Plane', viewCut=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=438.112, 
        farPlane=634.082, width=89.5407, height=49.8572, viewOffsetX=-15.098, 
        viewOffsetY=-43.3773)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=433.176, 
        farPlane=668.613, width=88.5319, height=49.2955, cameraPosition=(
        246.61, 397.498, 306.43), cameraUpVector=(-0.326294, -0.668022, 
        0.668789), cameraTarget=(22.8065, -4.10452, 56.8337), 
        viewOffsetX=-14.9279, viewOffsetY=-42.8885)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=433.269, 
        farPlane=668.519, width=88.5509, height=49.3061, cameraPosition=(
        247.022, 397.185, 306.563), cameraUpVector=(-0.318588, -0.672092, 
        0.668427), cameraTarget=(23.2188, -4.41711, 56.9669), 
        viewOffsetX=-14.9311, viewOffsetY=-42.8977)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=421.784, 
        farPlane=680.002, width=196.981, height=109.681, viewOffsetX=10.0325, 
        viewOffsetY=-19.6772)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        activeCutName='X-Plane', viewCut=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=426.96, 
        farPlane=678.545, width=199.398, height=111.027, cameraPosition=(
        545.958, 95.2016, -0.238111), cameraUpVector=(-0.199226, -0.299619, 
        0.933026), cameraTarget=(37.4792, -20.6863, 40.8683), 
        viewOffsetX=10.1556, viewOffsetY=-19.9187)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=426.481, 
        farPlane=679.025, width=199.174, height=110.902, cameraPosition=(
        544.757, 102.138, 4.4621), cameraUpVector=(-0.257542, -0.0321445, 
        0.965732), cameraTarget=(36.2783, -13.7499, 45.5685), 
        viewOffsetX=10.1442, viewOffsetY=-19.8964)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=436.755, 
        farPlane=668.75, width=132.674, height=73.8741, viewOffsetX=-2.17582, 
        viewOffsetY=-31.0646)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=442.177, 
        farPlane=662.857, width=134.321, height=74.7913, cameraPosition=(
        489.129, 66.2434, 263.267), cameraUpVector=(-0.699584, 0.145677, 
        0.699544), cameraTarget=(15.4417, -9.67705, 54.6366), 
        viewOffsetX=-2.20283, viewOffsetY=-31.4503)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=453.083, 
        farPlane=651.951, width=57.4946, height=32.0136, viewOffsetX=-26.6479, 
        viewOffsetY=-31.5905)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=467.076, 
        farPlane=667.382, width=59.2703, height=33.0023, cameraPosition=(
        510.488, -87.0356, 246.647), cameraUpVector=(-0.620206, 0.228445, 
        0.750438), cameraTarget=(27.21, -18.0747, 58.6129), 
        viewOffsetX=-27.4708, viewOffsetY=-32.5661)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1 ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells1)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#2 ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells1)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(viewCut=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=457.349, 
        farPlane=677.11, width=147.244, height=81.9869, viewOffsetX=-22.4673, 
        viewOffsetY=-27.1742)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=407.2, 
        farPlane=668.536, width=131.098, height=72.9969, cameraPosition=(
        373.581, 290.423, 270.698), cameraUpVector=(-0.77708, -0.0620185, 
        0.626339), cameraTarget=(-5.73534, 5.45659, 50.283), 
        viewOffsetX=-20.0037, viewOffsetY=-24.1945)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=408.359, 
        farPlane=667.375, width=155.808, height=86.7555, viewOffsetX=-44.924, 
        viewOffsetY=-38.3165)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=373.056, 
        farPlane=618.252, width=142.338, height=79.2554, cameraPosition=(
        110.908, 451.616, 199.7), cameraUpVector=(-0.156384, -0.520134, 
        0.839646), cameraTarget=(-21.8654, -39.6212, 78.3456), 
        viewOffsetX=-41.0403, viewOffsetY=-35.004)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=369.993, 
        farPlane=621.315, width=199.033, height=110.824, viewOffsetX=-40.4508, 
        viewOffsetY=-27.0016)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=372.542, 
        farPlane=651.04, width=200.404, height=111.587, cameraPosition=(238.05, 
        401.623, 231.507), cameraUpVector=(-0.454476, -0.43203, 0.778975), 
        cameraTarget=(-28.4708, -17.5455, 67.3904), viewOffsetX=-40.7295, 
        viewOffsetY=-27.1876)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=372.183, 
        farPlane=651.399, width=200.211, height=111.48, cameraPosition=(
        236.537, 408.56, 216.245), cameraUpVector=(-0.634156, -0.292955, 
        0.715559), cameraTarget=(-29.9839, -10.6081, 52.1288), 
        viewOffsetX=-40.6902, viewOffsetY=-27.1614)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=456.129, 
        farPlane=650.387, width=245.369, height=136.624, cameraPosition=(
        306.534, 84.9103, 466.251), cameraUpVector=(-0.957539, 0.0548957, 
        0.283029), cameraTarget=(-2.52535, 23.7454, 48.6253), 
        viewOffsetX=-49.8679, viewOffsetY=-33.2876)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=473.304, 
        farPlane=692.617, width=254.608, height=141.768, cameraPosition=(
        98.0049, -370.64, 454.096), cameraUpVector=(-0.64729, 0.696517, 
        0.309646), cameraTarget=(34.8985, -11.9693, 78.5396), 
        viewOffsetX=-51.7456, viewOffsetY=-34.541)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=462.445, 
        farPlane=680.311, width=248.766, height=138.516, cameraPosition=(
        333.206, -83.0499, 472.297), cameraUpVector=(-0.729373, 0.637839, 
        0.247339), cameraTarget=(52.9731, 34.9642, 46.6074), 
        viewOffsetX=-50.5584, viewOffsetY=-33.7485)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=452.092, 
        farPlane=690.663, width=372.23, height=207.262, viewOffsetX=-75.3257, 
        viewOffsetY=-49.3981)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=367.863, 
        farPlane=642.026, width=302.88, height=168.647, cameraPosition=(
        -90.8049, 471.719, 196.762), cameraUpVector=(-0.821926, -0.186419, 
        -0.538224), cameraTarget=(-22.4153, 32.8822, -79.6691), 
        viewOffsetX=-61.2919, viewOffsetY=-40.1948)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=390.102, 
        farPlane=619.787, width=227.045, height=126.421, viewOffsetX=-59.5025, 
        viewOffsetY=-33.878)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=392.137, 
        farPlane=593.365, width=228.23, height=127.081, cameraPosition=(
        163.287, -82.7696, 478.735), cameraUpVector=(-0.925379, 0.352037, 
        0.140513), cameraTarget=(-28.5973, 89.8044, 23.688), 
        viewOffsetX=-59.813, viewOffsetY=-34.0548)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=407.091, 
        farPlane=578.412, width=148.315, height=82.5835, viewOffsetX=-64.4039, 
        viewOffsetY=-7.91591)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=402.625, 
        farPlane=582.877, width=146.688, height=81.6777, viewOffsetX=-54.1633, 
        viewOffsetY=-39.6834)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=399.486, 
        farPlane=586.016, width=191.944, height=106.877, viewOffsetX=-50.5098, 
        viewOffsetY=-42.2396)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=371.222, 
        farPlane=632.208, width=178.364, height=99.3148, cameraPosition=(
        238.035, 320.812, 327.307), cameraUpVector=(-0.66134, -0.464078, 
        0.589289), cameraTarget=(-79.3216, 25.4935, 34.4912), 
        viewOffsetX=-46.9361, viewOffsetY=-39.251)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=385.853, 
        farPlane=617.577, width=91.8782, height=51.1587, viewOffsetX=-90.6043, 
        viewOffsetY=-26.5392)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=384.459, 
        farPlane=618.97, width=91.5464, height=50.974, viewOffsetX=-70.6418, 
        viewOffsetY=-29.8416)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=373.478, 
        farPlane=629.951, width=195.95, height=109.107, viewOffsetX=-74.6224, 
        viewOffsetY=-33.7108)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=370.498, 
        farPlane=632.931, width=194.386, height=108.236, viewOffsetX=-63.1977, 
        viewOffsetY=-33.4419)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    pickedRegions = c1.getSequenceFromMask(mask=('[#3f ]', ), )
    a.deleteMesh(regions=pickedRegions)
    a = mdb.models['3D_MODEL'].rootAssembly
    e1 = a.instances['soil-1'].edges
    pickedEdges = e1.getSequenceFromMask(mask=('[#24825b40 #21 ]', ), )
    a.seedEdgeBySize(edges=pickedEdges, size=2.0, deviationFactor=0.1, 
        minSizeFactor=0.1, constraint=FINER)
    a = mdb.models['3D_MODEL'].rootAssembly
    e1 = a.instances['soil-1'].edges
    edges1 = e1.getSequenceFromMask(mask=('[#24825b40 #21 ]', ), )
    a.Set(edges=edges1, name='soil_vertical_edges')


def sweeppath():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=391.306, 
        farPlane=625.636, width=351.274, height=195.593, viewOffsetX=-59.1031, 
        viewOffsetY=19.0951)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=408.38, 
        farPlane=608.562, width=209.432, height=116.614, viewOffsetX=-34.9767, 
        viewOffsetY=13.3424)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=405.402, 
        farPlane=611.541, width=207.905, height=115.764, viewOffsetX=14.1176, 
        viewOffsetY=7.26394)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=416.097, 
        farPlane=579.651, width=213.39, height=118.818, cameraPosition=(
        138.856, -125.04, 474.355), cameraUpVector=(-0.97241, 0.22949, 
        -0.0418656), cameraTarget=(9.9609, -1.02718, -17.2522), 
        viewOffsetX=14.49, viewOffsetY=7.45558)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=414.931, 
        farPlane=580.818, width=246.954, height=137.507, viewOffsetX=11.9869, 
        viewOffsetY=3.78465)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        seeds=OFF)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#3c ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells1)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.intersect(
        leaf=leaf)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.undoLast()
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#3c ]', ), )
    leaf = dgm.LeafFromGeometry(cellSeq=cells1)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.remove(leaf=leaf)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=379.454, 
        farPlane=636.327, width=225.839, height=125.75, cameraPosition=(
        437.144, -132.677, 234.687), cameraUpVector=(-0.65778, 0.322565, 
        0.680645), cameraTarget=(-9.59841, -0.718207, -3.38636), 
        viewOffsetX=10.962, viewOffsetY=3.46106)
    p1 = mdb.models['3D_MODEL'].parts['soil']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)


def geostatic():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.undoLast()
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.undoLast()
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.redoLast()
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#7f ]', ), )
    region = regionToolset.Region(cells=cells1)
    mdb.models['3D_MODEL'].GeostaticStress(name='geostatic_field', region=region, 
        stressMag1=0.0, vCoord1=6.0, stressMag2=800.0, vCoord2=20.0, 
        lateralCoeff1=0.5, lateralCoeff2=None)


def geostatic_step():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    mdb.models['3D_MODEL'].GeostaticStep(name='Step-4', previous='Initial')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-4')


def static():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    mdb.models['3D_MODEL'].StaticStep(name='static', previous='geostatic')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='static')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    i1 = mdb.models['3D_MODEL'].rootAssembly.allInstances['column-1']
    leaf = dgm.LeafFromInstance(instances=(i1, ))
    session.viewports['Viewport: 1'].assemblyDisplay.displayGroup.replace(
        leaf=leaf)
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['column-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#3 ]', ), )
    region = regionToolset.Region(cells=cells1)
    mdb.models['3D_MODEL'].Gravity(name='gravity_static', createStepName='static', 
        comp3=-1.0, distributionType=UNIFORM, field='', region=region)


def gravity_geo():
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
    del mdb.models['3D_MODEL'].loads['gravity_geostatic']
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='geostatic')
    a = mdb.models['3D_MODEL'].rootAssembly
    c1 = a.instances['soil-1'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#7f ]', ), )
    region = regionToolset.Region(cells=cells1)
    mdb.models['3D_MODEL'].Gravity(name='gravity_geostatic', 
        createStepName='geostatic', comp3=-9.81, distributionType=UNIFORM, 
        field='', region=region)


