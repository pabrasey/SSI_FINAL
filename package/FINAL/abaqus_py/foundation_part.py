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

def create_part(l, w, depth):
    s = mdb.models['3D_MODEL'].ConstrainedSketch(name='__profile__',
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(-l/2, -w/2), point2=(l/2, w/2))
    p = mdb.models['3D_MODEL'].Part(name='foundation', dimensionality=THREE_D,
        type=DEFORMABLE_BODY)
    p = mdb.models['3D_MODEL'].parts['foundation']
    p.BaseSolidExtrude(sketch=s, depth=depth)
    s.unsetPrimaryObject()
    p = mdb.models['3D_MODEL'].parts['foundation']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['3D_MODEL'].sketches['__profile__']
