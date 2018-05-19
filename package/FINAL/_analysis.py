from pprint import pprint
import json

from datetime import *


from analytical_solution.system import AnalyticalSystem


class Analysis:

    def __init__(self, model, results_dir):

        self.steel = model['steel']
        self.soil = model['soil']
        self.tube = model['tube']
        self.super_str = model['super_str']
        self.pile = model['pile']

        # identify the analysis with time
        n = datetime.now()
        self.analysisname = str(n.year) + '_' + str(n.month) + '_' + str(n.day) + '--' + str(n.hour) + '_' + str(n.minute) + '_' + str(n.microsecond)
        self.results_dir = results_dir

        # run the analysis
        self.print_objects()


    def run_analytical(self):
        self.analytical_system = AnalyticalSystem(column=self.super_str, foundation=self.pile,
                                                  soil=self.soil, analysisname=self.analysisname)


    def run_numerical(self):
        from abaqus_py.system import NumericalSystem
        self.numerical_system = NumericalSystem(steel=self.steel, soil=self.soil, super_str=self.super_str,
                                                foundation=self.pile,
                                                results_dir=self.results_dir + 'abaqus/', analysisname=self.analysisname)
        self.numerical_system.run_analysis()
        self.numerical_system.output()


    def save_object(self):
        # saves the Analysis object in file
        filename = self.results_dir + 'models/' + self.analysisname

        with open(filename, 'wb') as f:  # Overwrites any existing file.

            objects = [self.steel, self.soil, self.tube, self.super_str, self.pile, self.analytical_system.sdof]
            if hasattr(self, 'numerical_system'):
                objects += (self.numerical_system,)

            json.dump([obj.__dict__ for obj in objects], f, default=lambda x: x.__dict__, indent=4)


    def print_objects(self):
        print '------------------------------- MODEL --------------------------------------'
        print '\n Super Structure'
        pprint(vars(self.super_str))
        print '\n Pile'
        pprint(vars(self.pile))
        print '\n Tube Section'
        pprint(vars(self.tube))
        print '------------------------------ RESULTS -----------------------------------'
