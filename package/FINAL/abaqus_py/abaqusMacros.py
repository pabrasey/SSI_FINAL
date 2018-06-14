# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def steady_st():
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
    mdb.models['3D_MODEL'].SteadyStateModalStep(name='ssd', previous='frequency', 
        frequencyRange=((0.0, 10.0, 20, 3.0), ))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ssd')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='frequency')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='ssd')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=368.488, 
        farPlane=584.862, width=11.393, height=5.2084, viewOffsetX=16.1894, 
        viewOffsetY=36.063)
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['column-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#20 ]', ), )
    region = a.Surface(side1Faces=side1Faces1, name='top_surf')
    mdb.models['3D_MODEL'].SurfaceTraction(name='top_load', createStepName='ssd', 
        region=region, magnitude=1000+0j, directionVector=((-1.0, 0.0, 0.0), (
        -2.0, 0.0, 0.0)), distributionType=UNIFORM, field='', localCsys=None, 
        traction=GENERAL)


