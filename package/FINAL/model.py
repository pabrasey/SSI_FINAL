from math import *



class Material:

    def __init__(o, name, E, nu, rho, zeta):
        o.name = name
        o.E = E
        o.nu = nu
        o.rho = rho
        o.zeta = zeta

class Soil(Material, object):

    def __init__(o, name, E, nu, rho, zeta, phi):

        # create material
        super(Soil, o).__init__(name, E, nu, rho, zeta)

        # special properties of soil
        o.phi = phi
        o.G = o.E / (2 * (1 + o.nu))
        o.V_s = sqrt(o.G / o.rho)
        o.V_La = 3.4 / (pi * 1 - o.nu) * o.V_s


class HollowRoundSection:

    def __init__(o, d_e, t):
        o.d_e = d_e
        o.d = o.d_e   # used by Gazetas
        o.d_i = o.d_e - 2*t

        o.r_e = o.d_e / 2
        o.r_i = o.d_i / 2

        o.t = t
        o.A = pi * ( o.r_e**2 - o.r_i**2 )

        o.I_y = pi / 4 * ( o.r_e**4 - o.r_i**4 )


class Column:

    def __init__(o, material, section, height):

        o.mat = material
        o.sec = section
        o.h = height

        o.k = 3 * o.mat.E * o.sec.I_y / (o.h ** 3)   # N / m ^ 2 * m ^ 4 / m ^ 3 = N / m
        o.m = o.sec.A * o.h * o.mat.rho
