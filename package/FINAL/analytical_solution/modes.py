from math import *
import operator


''' ------------------- Modes  ------------------- '''
class Mode(object):

    def __init__(o, m, k, zeta):

        o.m = m
        o.k = k
        o.zeta = zeta

        o.omega_n = sqrt(o.k / o.m)
        o.f_n = o.omega_n / (2 * pi)
        if not hasattr(o, 'zeta'): # for foundation modes
            o.zeta = min(1, o.c / (2 * o.m * o.omega_n))
        o.omega_d = o.omega_n * sqrt(1 - o.zeta ** 2)


    def u(o, t, u0, v0):

        u = exp(-o.zeta * o.omega_n * t) * (
                    u0 * cos(o.omega_d * t) + (v0 + o.zeta * o.omega_n * u0) / o.omega_d * sin(o.omega_d * t))




''' ------------------- SDOF Mode  ------------------- '''

class Sdof(object):

    def __init__(o, H, zeta_mat, c_mode, h_mode, r_mode, m):
        # the first element in omega_ns is the one used specifically to calculate the damping ratio contribution of material

        o.H = H

        # extract properties from modes
        modes = (c_mode, h_mode, r_mode)
        o.m = m
        o.omega_ns = list(obj.omega_n for obj in modes)
        o.ks = (c_mode.k, h_mode.k, r_mode.k / o.H**2)
        o.zetas = list(obj.zeta for obj in modes)

        # compute system properties
        o.k = Sdof.prod(o.ks) / Sdof.sum_mult(o.ks)
        o.omega_n = sqrt(o.k / o.m)
        o.zeta =    (o.omega_n / c_mode.omega_n) ** 3 * c_mode.zeta + \
                    (o.omega_n / h_mode.omega_n) ** 3 * h_mode.zeta + \
                    (o.omega_n / r_mode.omega_n) ** 3 * r_mode.zeta + \
                    (1 - (o.omega_n / c_mode.omega_n) ** 2) * zeta_mat

        o.omega_d = o.omega_n * sqrt(1 - o.zeta ** 2)
        o.f_n = o.omega_n / (2 * pi)
        o.T_n = 1 / o.f_n

        # SSI Indexes
        o.SDR = o.zeta
        o.PLR = c_mode.omega_n / o.omega_n
        o.SSI_index = c_mode.k / o.k

    @staticmethod
    def prod(iterable):
        return reduce(operator.mul, iterable, 1)

    @staticmethod
    def sum_mult(matrix):
        m = matrix;
        i = 0;
        r = 0;
        while i < len(m):
            j = i + 1;
            while j < len(m):
                r = r + m[i] * m[j];
                j = j + 1;
            i = i + 1;
        return r
