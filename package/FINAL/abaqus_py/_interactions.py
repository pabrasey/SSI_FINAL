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

def interaction_soil_col(contact):
    create_surfaces()
    if contact:
        soil_col_contact()
    else:
        soil_col_tie()

def create_surfaces():
    # outter column-soil surface
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['column-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#2 ]',), )
    a.Surface(side1Faces=side1Faces1, name='col_soil_out_surf')
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['soil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#2000000 ]',), )
    a.Surface(side1Faces=side1Faces1, name='soil_col_out_surf')


    # inner column-soil surface
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['column-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#4 ]',), )
    a.Surface(side1Faces=side1Faces1, name='col_soil_in_surf')
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['soil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#4000000 ]',), )
    a.Surface(side1Faces=side1Faces1, name='soil_col_in_surf')

    # bottom column-soil surface
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['column-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#40 ]',), )
    a.Surface(side1Faces=side1Faces1, name='soil_col_bottom_surf')
    a = mdb.models['3D_MODEL'].rootAssembly
    s1 = a.instances['soil-1'].faces
    side1Faces1 = s1.getSequenceFromMask(mask=('[#8000000 ]',), )
    a.Surface(side1Faces=side1Faces1, name='col_soil_bottom_surf')


def soil_col_contact():
    # create contact property
    mdb.models['3D_MODEL'].ContactProperty('IntProp-1')
    mdb.models['3D_MODEL'].interactionProperties['IntProp-1'].NormalBehavior(
        pressureOverclosure=HARD, allowSeparation=ON,
        constraintEnforcementMethod=DEFAULT)
    mdb.models['3D_MODEL'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF,
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0,
        table=((0.5, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION,
        fraction=0.005, elasticSlipStiffness=None)

    # create surface to surface contacts

    # outter column-soil surface
    a = mdb.models['3D_MODEL'].rootAssembly
    region1 = a.surfaces['col_soil_out_surf']
    a = mdb.models['3D_MODEL'].rootAssembly
    region2 = a.surfaces['soil_col_out_surf']

    mdb.models['3D_MODEL'].SurfaceToSurfaceContactStd(name='Int-1',
        createStepName='Initial', master=region1, slave=region2,
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1',
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None,
        clearanceRegion=None)

    # inner column-soil surface
    a = mdb.models['3D_MODEL'].rootAssembly
    region1 = a.surfaces['col_soil_in_surf']
    a = mdb.models['3D_MODEL'].rootAssembly
    region2 = a.surfaces['soil_col_in_surf']

    mdb.models['3D_MODEL'].SurfaceToSurfaceContactStd(name='Int-2',
        createStepName='Initial', master=region1, slave=region2,
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1',
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None,
        clearanceRegion=None)

    # bottom column-soil surface
    a = mdb.models['3D_MODEL'].rootAssembly
    region1 = a.surfaces['col_soil_bottom_surf']
    a = mdb.models['3D_MODEL'].rootAssembly
    region2 = a.surfaces['soil_col_bottom_surf']

    mdb.models['3D_MODEL'].SurfaceToSurfaceContactStd(name='Int-3',
        createStepName='Initial', master=region1, slave=region2,
        sliding=FINITE, thickness=ON, interactionProperty='IntProp-1',
        adjustMethod=NONE, initialClearance=OMIT, datumAxis=None,
        clearanceRegion=None)


def soil_col_tie():
    # outter column-soil surface
    a = mdb.models['3D_MODEL'].rootAssembly
    region1=a.surfaces['col_soil_out_surf']
    a = mdb.models['3D_MODEL'].rootAssembly
    region2=a.surfaces['soil_col_out_surf']
    mdb.models['3D_MODEL'].Tie(name='Constraint-out', master=region1, slave=region2,
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON,
        thickness=ON)

    # outter column-soil surface
    a = mdb.models['3D_MODEL'].rootAssembly
    region1=a.surfaces['col_soil_in_surf']
    a = mdb.models['3D_MODEL'].rootAssembly
    region2=a.surfaces['soil_col_in_surf']
    mdb.models['3D_MODEL'].Tie(name='Constraint-in', master=region1, slave=region2,
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON,
        thickness=ON)

    # outter column-soil surface
    a = mdb.models['3D_MODEL'].rootAssembly
    region1=a.surfaces['col_soil_bottom_surf']
    a = mdb.models['3D_MODEL'].rootAssembly
    region2=a.surfaces['soil_col_bottom_surf']
    mdb.models['3D_MODEL'].Tie(name='Constraint-bottom', master=region1, slave=region2,
        positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON,
        thickness=ON)
