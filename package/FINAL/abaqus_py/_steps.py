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


def create_frequency(numEigen, minEigen, maxEigen):
    mdb.models['3D_MODEL'].FrequencyStep(name='frequency', previous='Initial',
        maxEigen=maxEigen, minEigen=minEigen, numEigen=numEigen)

def create_ini_disp():
    mdb.models['3D_MODEL'].StaticLinearPerturbationStep(name='ini_disp',
        previous='frequency')

def create_modal_dynamics(timePeriod, incSize):
    mdb.models['3D_MODEL'].ModalDynamicsStep(name='modal_dynamics',
        previous='ini_disp', timePeriod=timePeriod, incSize=incSize)
    # field output every 1 increament
    mdb.models['3D_MODEL'].fieldOutputRequests['F-Output-2'].setValues(frequency=1)
    mdb.models['3D_MODEL'].fieldOutputRequests['F-Output-3'].setValues(frequency=1)

def set_direct_damping(mode1, mode2, ratio):
    mdb.models['3D_MODEL'].steps['modal_dynamics'].setValues(directDamping=((mode1, mode2, ratio), ))
