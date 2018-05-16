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


def create_job(model, job):
    a = mdb.models[model].rootAssembly
    a.regenerate()
    mdb.Job(name=job, model=model, description='', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=4,
        numDomains=4, numGPUs=0)
    mdb.jobs[job].writeInput(consistencyChecking=OFF)

def modify_input_file(jobname):
    # Read in the file
    with open('job_acoustic.inp', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace('AC3D8', 'CIN3D8')

    # Write the file out again
    with open(jobname + '.inp', 'w') as file:
        file.write(filedata)

def import_input(jobname):
    mdb.ModelFromInputFile(name='Infinite_MODEL',
        inputFileName=jobname + '.inp')

    # show assembly in viewport
    a = mdb.models['Infinite_MODEL'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=274.947,
        farPlane=500.392, width=282.726, height=132.125, cameraPosition=(
        159.224, -339.94, 131.854), cameraUpVector=(-0.299384, 0.478845,
        0.825274), cameraTarget=(3.22106, -2.99207, 34.771))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=288.886,
        farPlane=484.63, width=297.06, height=138.824, cameraPosition=(
        -22.9693, -362.182, 168.722), cameraUpVector=(0.0268304, 0.640247,
        0.767701), cameraTarget=(1.39842, -3.21459, 35.1398))
