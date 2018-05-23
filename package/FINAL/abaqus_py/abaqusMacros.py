# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def fix_sides():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
        bcs=ON, predefinedFields=ON, connectors=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=319.092, 
        farPlane=533.427, width=195.079, height=119.929, cameraPosition=(
        278.422, -227.196, 239.289), cameraUpVector=(-0.719391, 0.340249, 
        0.605564), cameraTarget=(3.6561, -3.2647, 17.2793))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=329.718, 
        farPlane=523.272, width=201.575, height=123.923, cameraPosition=(
        365.595, 80.0089, 214.571), cameraUpVector=(-0.716193, -0.185844, 
        0.672703), cameraTarget=(5.29496, 2.51078, 16.8146))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=313.281, 
        farPlane=546.348, width=191.526, height=117.745, cameraPosition=(
        -110.32, 235.445, 352.253), cameraUpVector=(0.389513, -0.868752, 
        0.30586), cameraTarget=(-3.90962, 5.51705, 19.4775))
    a = mdb.models['3D_MODEL'].rootAssembly
    f1 = a.instances['soil-1'].faces
    faces1 = f1.getSequenceFromMask(mask=('[#20201100 ]', ), )
    region = a.Set(faces=faces1, name='soil_sides')
    mdb.models['3D_MODEL'].DisplacementBC(name='fixed_sides', 
        createStepName='Initial', region=region, u1=SET, u2=SET, u3=UNSET, 
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude=UNSET, 
        distributionType=UNIFORM, fieldName='', localCsys=None)


