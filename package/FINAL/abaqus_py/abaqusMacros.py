# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def u1_path():
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    cliCommand(
        """session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)""")
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        UNDEFORMED, ))
    session.Path(name='Path-2', type=POINT_LIST, expression=((-4.5, 0.0, 0.0), (
        -5.5, 0.0, 0.0), (-10.0, 0.0, 0.0), (-50.0, 0.0, 0.0), (-70.0, 0.0, 
        0.0), (-90.0, 0.0, 0.0), (-100.0, 0.0, 0.0)))
    xyp = session.xyPlots['XYPlot-1']
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    pth = session.paths['Path-2']
    xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
        projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
    c1 = session.Curve(xyData=xy1)
    chart.setValues(curvesToPlot=(c1, ), )
    session.viewports['Viewport: 1'].setValues(displayedObject=xyp)


def xy_plot():
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
    odb = session.odbs['C:/Users/braseyp/Dropbox/Civil Engineering/ETH/ETH_Projektarbeit_SSI_2018/Software/FINAL/SSI_FINAL/package/FINAL/abaqus_wd/job_infinite_2018_5_28--12_28_694000.odb']
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        DEFORMED, ))
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U2'), 
        )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), 
        )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
        'Magnitude'), )
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(COMPONENT, 'U1'), 
        )
    pth = session.paths['hor_soil_path']
    session.XYDataFromPath(name='XYData-3', path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
        projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
    xyp = session.xyPlots['XYPlot-1']
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    pth = session.paths['hor_soil_path']
    xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
        projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
    c1 = session.Curve(xyData=xy1)
    chart.setValues(curvesToPlot=(c1, ), )
    session.viewports['Viewport: 1'].setValues(displayedObject=xyp)


def sdfas():
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
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='geostatic')
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='static')
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='frequency')
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='static')
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='ini_disp')
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='frequency')


def sadf():
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
    odb = session.odbs['C:/Users/braseyp/Dropbox/Civil Engineering/ETH/ETH_Projektarbeit_SSI_2018/Software/FINAL/SSI_FINAL/package/FINAL/abaqus_wd/job_infinite_2018_5_28--19_45_802000.odb']
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='frequency', frame=1)
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='frequency', frame=2)
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step='frequency', frame=1)


