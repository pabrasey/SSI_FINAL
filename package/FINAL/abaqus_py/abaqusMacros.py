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


def tm():
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
    p = mdb.models['3D_MODEL'].parts['column']
    p.ReferencePoint(point=(0.0, 0.0, 120.0))
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['3D_MODEL'].parts['column']
    r = p.referencePoints
    refPoints=(r[3], )
    region=p.Set(referencePoints=refPoints, name='Set-1')
    mdb.models['3D_MODEL'].parts['column'].engineeringFeatures.PointMassInertia(
        name='Inertia-1', region=region, mass=210000.0, alpha=0.0, 
        composite=0.0)


def asdf():
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
    p = mdb.models['3D_MODEL'].parts['column']
    c = p.cells
    pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
    d = p.datums
    p.PartitionCellByDatumPlane(datumPlane=d[6], cells=pickedCells)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=218.478, 
        farPlane=305.465, width=64.4373, height=25.1612, viewOffsetX=-16.4499, 
        viewOffsetY=-9.14685)
    p = mdb.models['3D_MODEL'].parts['column']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#4 ]', ), )
    region=p.Set(cells=cells, name='Set-2')
    mdb.models['3D_MODEL'].parts['column'].engineeringFeatures.NonstructuralMass(
        name='Inertia-2', region=region, units=TOTAL_MASS, magnitude=210000.0, 
        distribution=VOLUME_PROPORTIONAL)


def sad():
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
    p1 = mdb.models['3D_MODEL'].parts['column']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    del mdb.models['3D_MODEL'].parts['column'].sets['col_set']
    p = mdb.models['3D_MODEL'].parts['column']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#7 ]', ), )
    region = p.Set(cells=cells, name='col_set')
    p = mdb.models['3D_MODEL'].parts['column']
    p.SectionAssignment(region=region, sectionName='column_section', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


def topm():
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
    session.viewports['Viewport: 1'].view.setValues(nearPlane=224.62, 
        farPlane=299.323, width=1.80547, height=0.885579, viewOffsetX=-35.129, 
        viewOffsetY=-21.5317)
    p = mdb.models['3D_MODEL'].parts['column']
    v = p.vertices
    verts = v.getSequenceFromMask(mask=('[#10 ]', ), )
    region=regionToolset.Region(vertices=verts)
    mdb.models['3D_MODEL'].parts['column'].engineeringFeatures.PointMassInertia(
        name='Inertia-1', region=region, mass=105000.0, alpha=0.0, 
        composite=0.0)


