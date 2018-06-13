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


def visual_dyn(analysisbasename):

    session.viewports['Viewport: 1'].view.setViewpoint(viewVector=(0, -1, 0.5),
        cameraUpVector=(0, 0, 1))
    session.viewports['Viewport: 1'].view.fitView()
    session.animationController.setValues(animationType=TIME_HISTORY, viewports=(
        'Viewport: 1', ))
    session.animationController.play(duration=UNLIMITED)
    session.imageAnimationOptions.setValues(vpDecorations=ON, vpBackground=OFF,
                                            compass=ON, frameRate=16)
    session.writeImageAnimation(
        fileName=analysisbasename,
        format=QUICKTIME, canvasObjects=(session.viewports['Viewport: 1'], ))


def freq(odb):

    step = odb.steps['frequency']
    region = step.historyRegions['Assembly ASSEMBLY']
    return {'freq' : region.historyOutputs['EIGFREQ'].data}


def soil_u(odb, x0, x1, analysisbasename):
    # create path
    pts_x = tuple( (x, 0.0, 0.0) for x in arange(-x0, -(x1 + 1), -1) )
    pts_y = tuple( (0.0, y, 0.0) for y in arange(-x0, -(x1 + 1), -1) )
    pth_x = session.Path(name='hor_soil_path_x', type=POINT_LIST, expression=pts_x)
    pth_y = session.Path(name='hor_soil_path_y', type=POINT_LIST, expression=pts_y)

    # create xy data
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='frequency', frame=1)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))

    ret = {}

    # U1 on x path
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'),
    )
    # save image
    session.viewports['Viewport: 1'].view.setViewpoint(viewVector=(0, -1, 0.5),
                                                       cameraUpVector=(0, 0, 1))
    session.viewports['Viewport: 1'].view.fitView()
    session.printToFile(analysisbasename + '_u1', PNG, (session.viewports['Viewport: 1'],))

    data = xyPlot.XYDataFromPath(path=pth_x, includeIntersections=False,
                                projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=int(x1-x0),
                                projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE)
    ret.update(create_xy_dict(data, 'soil_u1'))

    # U2 on y path
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'),
    )
    # save image
    session.viewports['Viewport: 1'].view.setViewpoint(viewVector=(-1, 0, 0.5),
                                                       cameraUpVector=(0, 0, 1))
    session.viewports['Viewport: 1'].view.fitView()
    session.printToFile(analysisbasename + '_u2', PNG, (session.viewports['Viewport: 1'],))

    data = xyPlot.XYDataFromPath(path=pth_y, includeIntersections=False,
                                 projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=int(x1-x0),
                                 projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE)
    ret.update(create_xy_dict(data, 'soil_u2'))

    # U3 on max of both
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U3'),
    )
    data3 = []
    data3.append(
        xyPlot.XYDataFromPath(path=pth_x, includeIntersections=False,
                                 projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=int(x1-x0),
                                 projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE)
    )
    data3.append(
        xyPlot.XYDataFromPath(path=pth_y, includeIntersections=False,
                                 projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=int(x1 - x0),
                                 projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE)
    )
    mx = [ max(map(abs, [d[1] for d in data3[0]] )) , max(map(abs, [d[1] for d in data3[1]] )) ]
    ind = mx.index(max(mx))
    ret.update(create_xy_dict(data3[ind], 'soil_u3'))

    return ret


def create_xy_dict(data, name):
    x_ = ()
    y_ = ()
    for d in data:
        x_ += (d[0],)
        y_ += (d[1],)

    return {name: (x_, y_)}
