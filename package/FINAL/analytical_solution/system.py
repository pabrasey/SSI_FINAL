from modes import *
from pprint import pprint

from math import *
from gazetas import HorizontalPile, RockPile


class AnalyticalSystem:

	def __init__(o, column, foundation, soil, analysisname):

		o.analysisname = analysisname

		o.h_foundation = HorizontalPile(foundation=foundation, soil=soil)
		o.r_foundation = RockPile(foundation=foundation, soil=soil)

		# Modes
		o.c_mode = Mode(m=column.m, k=column.k, zeta=column.mat.zeta)
		o.h_mode = Mode(m=o.h_foundation.m, k=o.h_foundation.k, zeta=o.h_foundation.zeta)
		o.r_mode = Mode(m=o.r_foundation.m, k=o.r_foundation.k, zeta=o.r_foundation.zeta)

		o.sdof = Sdof(H=(2.0/3.0*column.h), zeta_mat=0.0, c_mode=o.c_mode, h_mode=o.h_mode, r_mode=o.r_mode, m=(column.m + 2*foundation.m))


		# Initial conditions
		u0 = 0.30 # m
		v0 = 0.0 # m / s

		print '\n SDOF'
		pprint(vars(o.sdof))
		print '\n C Mode'
		pprint(vars(o.c_mode))
		print '\n H Mode'
		pprint(vars(o.h_mode))
		print '\n R Mode'
		pprint(vars(o.r_mode))
