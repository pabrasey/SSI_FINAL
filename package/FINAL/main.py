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

if one_analysis:

    '''------------------ Define Model ------------------'''

    # Materials
    steel = Material(name='steel', rho=7750, E=210.0e9, nu=0.30, zeta=0.0)
    soil = Soil(name='soil', rho=2000, E=87.5e6, nu=0.25, zeta=0.0,
                phi=45.0)  # Soil is a subclass of Material with special properties

    # Section
    tube = HollowRoundSection(d_e=4.0, t=0.05)

    # Parts
    super_str = Column(material=steel, section=tube, height=20)  # on soil
    pile = Column(material=steel, section=tube, height=5)  # in soil

    '''------------------ Create & Run Analysis ------------------'''

    model = {'steel': steel, 'soil': soil, 'tube': tube, 'super_str': super_str, 'pile': pile}

    analysis = Analysis(model, result_dir)
    analysis.run_analytical()
    analysis.run_numerical()
    analysis.save_object()

else:

    hs = ((5, 2), (10, 4), (20, 8), (40, 20), (60, 30))

    for h in hs:

        '''------------------ Define Model ------------------'''

        # Materials
        steel = Material(name='steel', rho=7750, E=210.0e9, nu=0.30, zeta=0.0)
        soil =  Soil    (name='soil', rho=2000, E=87.5e6, nu=0.25, zeta=0.0, phi=0) # Soil is a subclass of Material with special properties


        # Section
        tube = HollowRoundSection(d_e=4.0, t=0.05)


        # Parts
        super_str = Column(material=steel, section=tube, height=h[0]) # on soil
        pile = Column(material=steel, section=tube, height=h[1]) # in soil



        '''------------------ Create & Run Analysis ------------------'''

        model = {'steel': steel, 'soil': soil, 'tube': tube, 'super_str': super_str, 'pile': pile}

        analysis = Analysis(model, result_dir)
        analysis.run_analytical()
        analysis.run_numerical()
        analysis.save_object()
        analysis.numerical_system.delete_model() # needed to performe multiple analysis in a row
