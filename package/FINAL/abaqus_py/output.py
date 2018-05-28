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

from numpy import arange


def load_odb(jobname):
    session.openOdb(name=jobname + '.odb')
    odbName = jobname + '.odb'
    odb = session.odbs[odbName]
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)  # necessary !! even without gui
    return odb


def plot_top_disp(odb):

    data = session.xyDataListFromField(odb=odb, steps=('ini_disp', 'modal_dynamics', ), outputPosition=NODAL,
                                       variable=(('U', NODAL, ((INVARIANT, 'Magnitude'), (COMPONENT, 'U1'), (COMPONENT, 'U2'), )), ),
                                       nodePick=(('COLUMN-1', 1, ('[#10 ]', )), ), )
    x_ = ()
    y_ = ()
    for d in data[1]:
        x_ += (d[0],)
        y_ += (d[1],)

    return {'top_disp_1': (x_, y_)}


def visual(results_dir, analysisname):

    session.viewports['Viewport: 1'].view.setViewpoint(viewVector=(0, -1, 0.5),
        cameraUpVector=(0, 0, 1))
    session.viewports['Viewport: 1'].view.fitView()
    session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
        'Viewport: 1', ))
    session.animationController.play(duration=UNLIMITED)
    session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=OFF,
                                            compass=ON, frameRate=16)
    filename = results_dir + analysisname
    session.writeImageAnimation(
        fileName=filename,
        format=QUICKTIME, canvasObjects=(session.viewports['Viewport: 1'], ))


def freq(odb):

    step = odb.steps['frequency']
    region = step.historyRegions['Assembly ASSEMBLY']
    return {'freq' : region.historyOutputs['EIGFREQ'].data}


def soil_u1(odb, x0, x1):
    # create path
    points = tuple( (x, 0.0, 0.0) for x in arange(-x0, -x1, -1) )
    pth = session.Path(name='hor_soil_path', type=POINT_LIST, expression=points)

    # create xy data
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='frequency', frame=1)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF,))

    ret = {}

    # U1
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'),
    )
    data = xyPlot.XYDataFromPath(path=pth, includeIntersections=False,
                                projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=int(x1-x0),
                                projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
    ret.update(create_xy_dict(data, 'soil_u1'))

    # U2
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'),
    )
    data = xyPlot.XYDataFromPath(path=pth, includeIntersections=False,
                                 projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=int(x1-x0),
                                 projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
    ret.update(create_xy_dict(data, 'soil_u2'))

    # U3
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'),
    )
    data = xyPlot.XYDataFromPath(path=pth, includeIntersections=False,
                                 projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=int(x1-x0),
                                 projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
    ret.update(create_xy_dict(data, 'soil_u3'))

    return ret


def create_xy_dict(data, name):
    x_ = ()
    y_ = ()
    for d in data:
        x_ += (d[0],)
        y_ += (d[1],)

    return {name: (x_, y_)}
