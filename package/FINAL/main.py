import os, sys

# start this file from abaqus_wd so that all files from abaqus are saved their
# here add the path of the main.py file to the python path
abspath = os.path.abspath('../main.py')
dname = os.path.dirname(abspath)
sys.path.append(dname)
result_dir = '../results/'

from model import Material, HollowRoundSection, Column, Soil
from _analysis import Analysis

one_analysis = True

# Materials
steel = Material(name='steel', rho=7750, E=210.0e9, nu=0.30, zeta=0.0)
soil = Soil(name='soil', rho=2000, E=87.5e6, nu=0.25, zeta=0.0,
            phi=False)  # Soil is a subclass of Material with special properties

# Section
tube = HollowRoundSection(d_e=4.0, t=0.05)

if one_analysis:

    '''------------------ Define Model ------------------'''

    # Parts
    super_str = Column(material=steel, section=tube, height=80)  # on soil
    pile = Column(material=steel, section=tube, height=70)  # in soil

    '''------------------ Create & Run Analysis ------------------'''

    model = {'steel': steel, 'soil': soil, 'tube': tube, 'super_str': super_str, 'pile': pile}

    analysis = Analysis(model, result_dir)
    analysis.run_analytical()
    analysis.run_numerical()
    analysis.save_object()

else:

    ph = (20, 25, 30, 40, 50, 61, 71)

    for h in ph:

        '''------------------ Define Model ------------------'''

        # Parts
        super_str = Column(material=steel, section=tube, height=80) # on soil
        pile = Column(material=steel, section=tube, height=h) # in soil


        '''------------------ Create & Run Analysis ------------------'''

        model = {'steel': steel, 'soil': soil, 'tube': tube, 'super_str': super_str, 'pile': pile}

        analysis = Analysis(model, result_dir)
        analysis.run_analytical()
        try:
            analysis.run_numerical()
        except Exception as e:
            print >> sys.__stdout__, e
            continue
        analysis.save_object()
        analysis.numerical_system.delete_model() # needed to performe multiple analysis in a row
