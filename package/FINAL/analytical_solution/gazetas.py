from math import *

''' ------------------- Foundation Modes  ------------------- '''

class FoundationMode(object):

    def __init__(o, foundation, soil, a0):

        # assign foundation, soil and a0 to mode object
        o.f = foundation
        o.s = soil
        o.m = o.f.m
        o.a0 = a0


class HorizontalPile(FoundationMode, object):

    def __init__(o, foundation, soil):

        # call superclass constructor
        super(HorizontalPile, o).__init__ (foundation, soil, 0.0)

        o.k = o.stiffness(d=o.f.sec.d, E_p=o.f.mat.E, E_s_=o.s.E)
        o.compute_damp()


    def stiffness(o, d, E_p, E_s_):

        o.k_st = 0.6 * d * E_s_ * (E_p / E_s_)**0.35
        o.k_co = 1
        o.k_dyn = o.k_co * o.k_st
        return o.k_dyn


    def compute_damp(o):

        o.zeta = 0



class RockPile(FoundationMode, object):

    def __init__(o, foundation, soil):

        # call superclass constructor
        super(RockPile, o).__init__ (foundation, soil, 0.0)

        o.k = o.stiffness(d=o.f.sec.d, E_p=o.f.mat.E, E_s_=o.s.E)
        o.compute_damp()


    def stiffness(o, d, E_p, E_s_):

        o.k_st = 0.15 * d**3 * E_s_ * (E_p / E_s_)**0.80
        o.k_co = 1
        o.k_dyn = o.k_co * o.k_st
        return o.k_dyn


    def compute_damp(o):

        o.zeta = 0
