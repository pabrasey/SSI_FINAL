from modes import *
from pprint import pprint

from math import *
from gazetas import HorizontalPile, RockPile


class AnalyticalSystem:

	def __init__(o, super_str, foundation, soil, analysisname):

		o.analysisname = analysisname

		o.h_foundation = HorizontalPile(foundation=foundation, soil=soil)
		o.r_foundation = RockPile(foundation=foundation, soil=soil)

		# Modes
		o.c_mode = Mode(m=super_str.m, k=super_str.k, zeta=super_str.mat.zeta)
		o.h_mode = Mode(m=o.h_foundation.m, k=o.h_foundation.k, zeta=o.h_foundation.zeta)
		o.r_mode = Mode(m=o.r_foundation.m, k=o.r_foundation.k, zeta=o.r_foundation.zeta)

		o.sdof = Sdof(H=0.9*super_str.h, zeta_mat=0.0, c_mode=o.c_mode, h_mode=o.h_mode, r_mode=o.r_mode,
					  m=(super_str.m + super_str.topmass), pile_active_l=o.h_foundation.active_l)

		# Initial conditions
		u0 = super_str.h / 300 # m
		v0 = 0.0 # m / s

		#x_ = arange(0, 1, 0.01)
		#y_ = [ o.sdof.u(x, u0, v0) for x in x_ ]


	def print_objects(o):

		print '\n SDOF'
		pprint(vars(o.sdof))
		print '\n C Mode'
		pprint(vars(o.c_mode))
		print '\n H Mode'
		pprint(vars(o.h_mode))
		print '\n R Mode'
		pprint(vars(o.r_mode))
