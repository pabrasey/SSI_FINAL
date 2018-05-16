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


def create_soil_section():
    mdb.models['3D_MODEL'].HomogeneousSolidSection(name='soil_section',
                                               material='soil', thickness=None)


def create_column_section():
    mdb.models['3D_MODEL'].HomogeneousSolidSection(name='column_section',
                                                   material='steel', thickness=None)

def assign_section():
    # column
    p = mdb.models['3D_MODEL'].parts['column']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#3 ]', ), )
    region = p.Set(cells=cells, name='col_set')
    p = mdb.models['3D_MODEL'].parts['column']
    p.SectionAssignment(region=region, sectionName='column_section', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)

    # soil
    p = mdb.models['3D_MODEL'].parts['soil']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#7f ]', ), )
    region = p.Set(cells=cells, name='all_soil_set')
    p = mdb.models['3D_MODEL'].parts['soil']
    p.SectionAssignment(region=region, sectionName='soil_section', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)
