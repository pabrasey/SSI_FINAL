from abaqus import *
from abaqusConstants import *
import __main__

import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import _assembly
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

def create(mat):
    # elasticity
    mdb.models['3D_MODEL'].Material(name=mat.name)
    mdb.models['3D_MODEL'].materials[mat.name].Density(table=((mat.rho, ), ))
    mdb.models['3D_MODEL'].materials[mat.name].Elastic(table=((mat.E, mat.nu), ))
    mdb.models['3D_MODEL'].materials[mat.name].Damping()

    # plasticity
    if hasattr(mat, 'phi') and mat.phi > 0:
        mdb.models['3D_MODEL'].materials[mat.name].MohrCoulombPlasticity(table=((mat.phi, 0.0), ))
        mdb.models['3D_MODEL'].materials[mat.name].mohrCoulombPlasticity.MohrCoulombHardening(
            table=((1, 0.1), (0.0, 0.0001)))
        mdb.models['3D_MODEL'].materials[mat.name].mohrCoulombPlasticity.TensionCutOff(
            temperatureDependency=OFF, dependencies=0, table=((0.0, 0.0), ))
