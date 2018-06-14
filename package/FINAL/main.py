import os, sys

# start this file from abaqus_wd so that all files from abaqus are saved their
# here add the path of the main.py file to the python path
abspath = os.path.abspath('../main.py')
dname = os.path.dirname(abspath)
sys.path.append(dname)
result_dir = '../results/'

from model import Material, HollowRoundSection, Column, Soil
from _analysis import Analysis


'''------------------ DEFAULT PARAMETERS (can be changed bellow) ------------------'''

# Materials
steel = Material(name='steel', rho=7750, E=210.0e9, nu=0.30, zeta=0.0)
soil = Soil(name='soil', rho=2000, E=175e6, nu=0.25, zeta=0.0,
            phi=False, diameter=400, depth=100)  # Soil is a subclass of Material with special properties
                                                # soil without failure criterion if phi set to False

# Section
tube = HollowRoundSection(d_e=6.0, t=0.0025)

# Parts
super_str = Column(material=steel, section=tube, height=80, topmass=210e3)  # on soil
pile = Column(material=steel, section=tube, height=35)  # in soil


'''------------------ FUNCTIONS TO START ANALYSES ------------------'''

def one_analysis():
    soil = Soil(name='soil', rho=2000, E=175e6, nu=0.25, zeta=0.0, phi=False, diameter=400, depth=100)
    tube = HollowRoundSection(d_e=6.0, t=0.05)
    super_str = Column(material=steel, section=tube, height=80, topmass=210e3)  # on soil
    pile = Column(material=steel, section=tube, height=35)  # in soil

    model = {'steel': steel, 'soil': soil, 'tube': tube, 'super_str': super_str, 'pile': pile}
    analysis = Analysis(model, result_dir, serie_id='1')
    analysis.run_analytical()
    analysis.run_numerical()
    analysis.save_object()

one_analysis()


def serie_analyses(analysis):
    analysis.run_analytical()
    try:
        analysis.run_numerical()
    except Exception as e:
        print >> sys.__stdout__, e
    analysis.save_object()
    analysis.numerical_system.delete_model()  # needed to perform multiple analysis in a row


'''------------------ SERIE ANALYSES ------------------'''

''' ---- Soil diameter ---- '''

def soil_diameter_analysis():
    d_ = (600,)

    for d in d_:
        soil = Soil(name='soil', rho=2000, E=175e6, nu=0.25, zeta=0.0, phi=False, diameter=d, depth=100)
        tube = HollowRoundSection(d_e=6.0, t=0.0025)
        super_str = Column(material=steel, section=tube, height=80, topmass=210e3)
        pile = Column(material=steel, section=tube, height=35)

        model = {'steel': steel, 'soil': soil, 'tube': tube, 'super_str': super_str, 'pile': pile}
        serie_id = 'Sd_Ph' + str(int(pile.h)) + '_Pd' + str(int(tube.d_e)) + '_Pt' + str(tube.t) + '_Ch' + str(int(super_str.h)) + '_SE' + str(int(soil.E/1e6))
        analysis = Analysis(model, result_dir, serie_id=serie_id)
        serie_analyses(analysis)

#soil_diameter_analysis()


''' ---- Soil modulus ---- '''

def soil_modulus_analysis():
    E_ = (50, 300, 500, 700, 1000)

    for E in E_:
        soil = Soil(name='soil', rho=2000, E=E*1e6, nu=0.25, zeta=0.0, phi=False, diameter=400, depth=100)

        model = {'steel': steel, 'soil': soil, 'tube': tube, 'super_str': super_str, 'pile': pile}
        serie_id = 'SE_Ph' + str(int(pile.h)) + '_Pd' + str(int(tube.d_e)) + '_Pt' + str(tube.t) + '_Ch' + str(int(super_str.h)) + '_Sd' + str(int(soil.diameter))
        analysis = Analysis(model, result_dir, serie_id=serie_id)
        serie_analyses(analysis)

#soil_modulus_analysis()


''' ---- Pile's depth ---- '''

def ph_analysis(): # variable pile's depth

    ph = (20, 40, 61)
    SE = (250, 175, 50) # corresponding G : 100, 70, 20

    for E in SE:

        soil = Soil(name='soil', rho=2000, E=E*1e6, nu=0.25, zeta=0.0, phi=False, diameter=400, depth=100)

        for h in ph:

            pile = Column(material=steel, section=tube, height=h) # in soil

            model = {'steel': steel, 'soil': soil, 'tube': tube, 'super_str': super_str, 'pile': pile}
            analysis = Analysis(model, result_dir, serie_id='Ph_Pd6_H80_SE175_Sd400_')
            #analysis.run_analytical()
            #analysis.save_object()
            serie_analyses(analysis)

#ph_analysis()


''' ---- Tube diameter ---- '''

def pd_analysis(): # variable pile's diameter

    pd = (2.0, 4.0, 6.0, 8.0, 10.0)

    for d in pd:
        tube = HollowRoundSection(d_e=d, t=0.0025)
        super_str = Column(material=steel, section=tube, height=80, topmass=210e3)  # on soil
        pile = Column(material=steel, section=tube, height=35)  # in soil

        model = {'steel': steel, 'soil': soil, 'tube': tube, 'super_str': super_str, 'pile': pile}
        analysis = Analysis(model, result_dir, serie_id='Pd_Ph35_Ch80_SE175_Sd400')
        serie_analyses(analysis)

#pd_analysis()


''' ---- Structure's height ---- '''

def ch_analysis(): # variable super structure height

    ch = (40, 60, 80, 100)

    for h in ch:
        super_str = Column(material=steel, section=tube, height=h, topmass=210e3)

        model = {'steel': steel, 'soil': soil, 'tube': tube, 'super_str': super_str, 'pile': pile}
        analysis = Analysis(model, result_dir, serie_id='Ch_Ph35_Pd6_SE175_Sd400')
        serie_analyses(analysis)

#ch_analysis()
