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


def freq_analysis(numEigen, minEigen, maxEigen):
    # frequency step
    mdb.models['3D_MODEL'].FrequencyStep(name='frequency', previous='Initial',
        maxEigen=maxEigen, minEigen=minEigen, numEigen=numEigen)


def steady_state_dyn():
    # steady state dynamics, modal -> has to be after the frequency step
    mdb.models['3D_MODEL'].SteadyStateModalStep(name='ssd', previous='frequency',
                                                frequencyRange=((0.0, 10.0, 20, 3.0),))


def mod_dyn(timePeriod, incSize, numEigen, minEigen, maxEigen):
    # geostatic
    mdb.models['3D_MODEL'].GeostaticStep(name='geostatic', previous='Initial', timeIncrementationMethod=FIXED )

    # static
    mdb.models['3D_MODEL'].StaticStep(name='static', previous='geostatic')

    # frequency
    mdb.models['3D_MODEL'].FrequencyStep(name='frequency', previous='static',
                                         maxEigen=maxEigen, minEigen=minEigen, numEigen=numEigen)

    # initial displacement
    mdb.models['3D_MODEL'].StaticLinearPerturbationStep(name='ini_disp',
                                                        previous='frequency')

    # modal dynamics
    mdb.models['3D_MODEL'].ModalDynamicsStep(name='modal_dynamics',
                                             previous='ini_disp', timePeriod=timePeriod, incSize=incSize)
    # field output every 1 increment
    mdb.models['3D_MODEL'].fieldOutputRequests['F-Output-3'].setValues(frequency=1)
    mdb.models['3D_MODEL'].fieldOutputRequests['F-Output-4'].setValues(frequency=1)



def set_direct_damping(mode1, mode2, ratio):
    mdb.models['3D_MODEL'].steps['modal_dynamics'].setValues(directDamping=((mode1, mode2, ratio), ))
