import json
import os, glob
from collections import OrderedDict
from itertools import groupby
import copy
from moviepy.editor import VideoFileClip
from prettytable import PrettyTable
import decimal
import pyglet
from pylab import plot, show, title, xlabel, ylabel, legend
import pylab as plt
import frequency

''' ---------------------- FUNCTIONS TO GET DATA ---------------------- '''

def show_table(data, file=False):

    t = PrettyTable(data[0].keys())
    for row in data:
        t.add_row(row.values())
    t.sortby = "s_id"
    print(t)

    if file:
        with open('results/summary.txt', 'w') as f:
            f.write(t.get_string())


def get_data(filenames):
    data = []
    for filename in filenames:
        # model data
        with open(model_dir + filename + '.txt', 'r') as f:  # model
            objects = json.load(f, parse_float=lambda s: decimal.Decimal(str(round(float(s), 4))))
            l = len(objects)
            if objects[0].has_key('serie_id'):
                [lysis, steel, soil, tube, super_str, pile, sdof] = objects[:7]
            else:
                [steel, soil, tube, super_str, pile, sdof] = objects[:6]
                lysis = {}
                lysis['serie_id'] = 'NaN'
            # keys that have been added later in the code
            if not 'pile_active_l' in sdof: sdof['pile_active_l'] = 'NaN'

        dic = OrderedDict([
            ('name'      ,   filename),
            ('s_id'      ,   lysis['serie_id']),
            ('s_str_h'   ,   super_str['h']),
            ('G_soil'    ,   float(soil['G']) / 1e6),
            ('pile_depth',   pile['h']),
            ('pile_act_l',   sdof['pile_active_l']),
            ('d_e'       ,   tube['d_e']),
            ('t'         ,   tube['t']),
            ('Gaz. f_n'  ,   "%.3f" % sdof['f_n']),
        ])

        # abaqus results

        abq_res = get_abq_data(filename)
        if len(abq_res) > 0:
            n_sys = objects[l - 1]
            f_n = abq_res['freq'][0][1]
            # soil displacement
            if abq_res.has_key('soil_u2'):
                soil_u = [ abq_res['soil_u1'], abq_res['soil_u2'], abq_res['soil_u3'] ]
                mx = [max( map(abs, u[1]) ) for u in soil_u] # max displacement in each direction
                dof = mx.index(max( mx )) # direction of max displacement
                #soilU_ratio = "%.3f" % (soil_u[dof][1][-1] / soil_u[dof][1][0])
                soilU_ratio = "%.1f" % abs(soil_u[2][1][-1] / soil_u[2][1][0])
            else:
                dof = -1
                soilU_ratio = 'NaN'
            if not sdof.has_key('f_col'):
                sdof['f_col'] = 0
            if not sdof.has_key('k_col'):
                sdof['k_col'] = 0
            if not n_sys.has_key('duration'):
                n_sys['duration'] = 'NaN'

            dic.update([
                ('Abq f_n'   ,   "%.3f" % f_n),
                ('contact'   ,   n_sys['contact_col_soil']),
                ('phi'       ,   soil['phi']),
                ('soil_depth',   n_sys['soil_depth']),
                ('soil_width',   n_sys['soil_diameter']),
                ('soil_mesh' ,   n_sys['soil_mesh_size']),
                ('fix_sides' ,   n_sys['fixed_sides']),
                ('soilU_oi'  ,   soilU_ratio),
                ('PLR'       ,   "%.2f" % (float(sdof['f_col']) / float(f_n)) ),
                ('time [min]',   "%.0f" % n_sys['duration']),
            ])
        else:
            dic.update([
                ('Abq f_n',      'NaN'),
                ('contact',      'NaN'),
                ('phi',          'NaN'),
                ('soil_depth',   'NaN'),
                ('soil_width',   'NaN'),
                ('soil_mesh',    'NaN'),
                ('fix_sides',    'NaN'),
                ('soilU_oi',     'NaN'),
                ('PLR',          'NaN'),
                ('time [min]',   'NaN'),
            ])

        data.append(dic) # add to list of data

    return data


def get_abq_data(filename):
    data = {}
    abq_basename = abaqus_dir + filename
    if os.path.isfile(abq_basename + '.txt'):
        with open(abaqus_dir + filename + '.txt', 'r') as fa:
            data = json.load(fa, parse_float=lambda s: decimal.Decimal(str(round(float(s), 4))))
    return data


def plot_soil_u(analysisname):
    abq_res = get_abq_data(analysisname)
    soil_u1 = abq_res['soil_u1']
    plot_xy(soil_u1[0], soil_u1[1], 'U1', 'x [m] (path)', 'U [m]', False, annote=False)
    soil_u2 = abq_res['soil_u2']
    plot_xy(soil_u2[0], soil_u2[1], 'U2', 'x [m] (path)', 'U [m]', False, annote=False)
    soil_u3 = abq_res['soil_u3']
    plot_xy(soil_u3[0], soil_u3[1], 'U3', 'x [m] (path)', 'U [m]', True, title=analysisname, annote=False)

''' ---------------------- FUNCTIONS FOR ANALYSES ---------------------- '''

def param_analysis(data, x, y, discarded, needed):
    full_data = copy.deepcopy(data)
    data = copy.deepcopy(data)

    # remove the x, y and discarded keys in data
    for d in data:
        del d[x], d[y], d['name'], d['time [min]']
        for disc in discarded:
            del d[disc]

    # get the duplicates
    dupe_ind = [n for n, e in enumerate(data) if e in data[:n] + data[n+1:]]

    # create list of dupes containing the whole data
    # and remove entries that do not have the needed arguments
    full_dupes = []
    i = 0
    for n in dupe_ind:
        full_dupes.append(full_data[n])
        for need in needed:
            if not full_dupes[i][need[0]] == need[1]:
                del full_dupes[i]
                i -= 1
                break
        i += 1

    # create plot data
    xy_ = []
    for d in full_dupes:
        xy_.append((d[x], d[y]))

    x_ = [ xy_s[0] for xy_s in sorted(xy_) ]
    y_ = [ xy_s[1] for xy_s in sorted(xy_) ]

    return (x_, y_)


def plot_xy(x, y, label, xlab, ylab, show_, title='', annote=True):
    plot(x, y, label=label)
    if annote: # annote each point with the y value
        for xy in zip(x, y):
            plt.annotate( xy[1], xy=xy, textcoords='data')
    if show_:
        plt.title(title)
        legend(framealpha=1, frameon=True, ncol=1, fancybox=True, loc="best"); # name of the curve
        xlabel(xlab)
        ylabel(ylab)
        show()


def show_graphics(filename):

    print(filename)
    top_disp_1 = get_abq_data(filename)['top_disp_1']
    frequency.plot_results(top_disp_1[0], top_disp_1[1])

    abq_basename = abaqus_dir + filename

    if os.path.isfile(abq_basename + '.mov') or os.path.isfile(abq_basename + '.gif'):
        if not os.path.isfile(abq_basename + '.gif'):
            #create gif if doesn't exists
            VideoFileClip(abq_basename + '.mov').write_gif(abq_basename + '.gif')
            os.remove(abq_basename + '.mov')
        #show_gif(abq_basename + '.gif')

    print('')


def show_gif(filename):

    # pick an animated gif file you have in the working directory
    animation = pyglet.resource.animation(filename)
    sprite = pyglet.sprite.Sprite(animation)
    # create a window and set it to the image size
    win = pyglet.window.Window(width=sprite.width, height=sprite.height)
    # set window background color = r, g, b, alpha
    # each value goes from 0.0 to 1.0
    green = 0, 1, 0, 1
    pyglet.gl.glClearColor(*green)

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()
    pyglet.app.run()


''' ---------------------- GET RESULTS ---------------------- '''

model_dir = 'results/models/'
abaqus_dir = 'results/abaqus/'

filenames = sorted([os.path.basename(os.path.splitext(x)[0]) for x in glob.glob(model_dir + '2018_6*')])
filenames.sort(key=lambda x: os.path.getmtime(model_dir + x + '.txt'))

data = get_data(filenames)
show_table(data, file=True)

''' ---------------------- ANALYSES ---------------------- '''

''' ---- Soil width ---- '''

def soil_width_analysis():
    xy1 = param_analysis(data, 'soil_width', 'Abq f_n',
                   ['contact', 'soil_mesh', 'pile_act_l'],
                   [('s_str_h', 80), ('soil_depth', 60), ('fix_sides', True), ])
    xy2 = param_analysis(data, 'soil_width', 'Abq f_n',
                   ['contact', 'soil_mesh', 'pile_act_l'],
                   [('s_str_h', 80), ('soil_depth', 60), ('fix_sides', False), ])
    plot_xy(xy1[0], xy1[1], label='fixed sides', xlab='Soil Width [m]', ylab='Abaqus Frequency [Hz]', show_=False)
    plot_xy(xy2[0], xy2[1], label='infinite sides', xlab='Soil Width [m]', ylab='Abaqus Frequency [Hz]', show_=True)

#soil_width_analysis()


def soil_width_analysis1():
    xy1 = param_analysis(data, 'soil_width', 'Abq f_n',
                        discarded=['PLR'],
                        needed=[('s_id', 'Sd_Ph35_Pd6_Pt0.0025_Ch80_SE175')])
    xy2 = param_analysis(data, 'soil_width', 'Abq f_n',
                         discarded=['PLR', 'soilU_oi'],
                         needed=[('s_id', 'Sd_Ph35_Pd6_Pt0.05_Ch80_SE50')])
    plot_xy(xy1[0], xy1[1], 't = 0.0025 m, G = 70', xlab='Soil Diameter [m]', ylab='Abaqus First Frequency [Hz]', show_=False)
    plot_xy(xy2[0], xy2[1], 't = 0.05 m,   G = 100', xlab='Soil Diameter [m]', ylab='Abaqus First Frequency [Hz]', show_=True)

soil_width_analysis1()


def ratio_io_analysis():
    xy3 = param_analysis(data, 'pile_depth', 'soilU_oi',
                   ['contact', 'soil_depth', 'pile_act_l', 'Abq f_n'],
                   [('s_id', 'Ph+20_Sw300')])
    plot_xy(xy3[0], xy3[1], 'Ratio U3 boundary/center', 'Pile Length', 'Ratio', True)

#ratio_io_analysis()

''' ---- Pile's depth ---- '''

def freq_Ph():
    xy1 = param_analysis(data, 'pile_depth', 'Abq f_n',
                       ['PLR', 'Gaz. f_n'],
                       [('s_id', 'Ph_Pd6_H80_SE250_Sd400_')])
    xy2 = param_analysis(data, 'pile_depth', 'Abq f_n',
                         ['PLR', 'Gaz. f_n'],
                         [('s_id', 'Ph_Pd6_H80_SE175_Sd400_')])
    xy3 = param_analysis(data, 'pile_depth', 'Abq f_n',
                         ['PLR', 'Gaz. f_n'],
                         [('s_id', 'Ph_Pd6_H80_SE50_Sd400_')])
    plot_xy(xy1[0], xy1[1], 'G_soil=100Mpa', xlab='Pile Length [m]', ylab='Abaqus Frequency [Hz]', show_=False)
    plot_xy(xy2[0], xy2[1], 'G_soil=70pa', xlab='Pile Length [m]', ylab='Abaqus Frequency [Hz]', show_=False)
    plot_xy(xy3[0], xy3[1], 'G_soil=20Mpa', xlab='Pile Length [m]', ylab='Abaqus Frequency [Hz]', show_=True)

#freq_Ph()


def PLR_Ph():
    xy1 = param_analysis(data, 'pile_depth', 'PLR',
                         discarded=['Abq f_n', 'Gaz. f_n'],
                         needed=[('s_id', 'Ph_Pd6_H80_SE250_Sd400_')])
    xy2 = param_analysis(data, 'pile_depth', 'PLR',
                         discarded=['Abq f_n', 'Gaz. f_n'],
                         needed=[('s_id', 'Ph_Pd6_H80_SE175_Sd400_')])
    xy3 = param_analysis(data, 'pile_depth', 'PLR',
                         discarded=['Abq f_n', 'Gaz. f_n'],
                         needed=[('s_id', 'Ph_Pd6_H80_SE50_Sd400_')])
    plot_xy(xy1[0], xy1[1], 'G_soil=100Mpa', xlab='Pile Length [m]', ylab='PLR', show_=False)
    plot_xy(xy2[0], xy2[1], 'G_soil=70pa', xlab='Pile Length [m]', ylab='PLR', show_=False)
    plot_xy(xy3[0], xy3[1], 'G_soil=20Mpa', xlab='Pile Length [m]', ylab='PLR', show_=True)

#PLR_Ph()



''' ---- Tube diameter ---- '''

def freq_Pd():
    xy1 = param_analysis(data, 'd_e', 'Abq f_n',
                        discarded=['PLR', 'Gaz. f_n', 'pile_act_l'],
                        needed=[('s_id', 'Pd_Ph35_Ch80_SE175_Sd400')])
    xy2 = param_analysis(data, 'd_e', 'Gaz. f_n',
                         discarded=['PLR', 'Abq f_n', 'pile_act_l'],
                         needed=[('s_id', 'Pd_Ph35_Ch80_SE175_Sd400')])
    plot_xy(xy1[0], xy1[1], 'Abaqus', xlab='Pile Diameter [m]', ylab='Frequency [Hz]', show_=False)
    plot_xy(xy2[0], xy2[1], 'Gazetas', xlab='Pile Diameter [m]', ylab='Frequency [Hz]', show_=True)

#freq_Pd()

def PLR_Pd():
    xy1 = param_analysis(data, 'd_e', 'PLR',
                        discarded=['Abq f_n', 'Gaz. f_n', 'pile_act_l'],
                        needed=[('s_id', 'Pd_Ph35_Ch80_SE175_Sd400')])
    plot_xy(xy1[0], xy1[1], 'G_soil=70Mpa', xlab='Pile Diameter [m]', ylab='PLR', show_=True)

#PLR_Pd()

''' ---- Structure's height ---- '''

def freq_Pd():
    xy1 = param_analysis(data, 's_str_h', 'Abq f_n',
                        discarded=['PLR', 'Gaz. f_n',],
                        needed=[('s_id', 'Ch_Ph35_Pd6_SE175_Sd400')])
    xy2 = param_analysis(data, 's_str_h', 'Gaz. f_n',
                         discarded=['PLR', 'Abq f_n', 'pile_act_l'],
                         needed=[('s_id', 'Ch_Ph35_Pd6_SE175_Sd400')])
    plot_xy(xy1[0], xy1[1], 'Abaqus', xlab='Structure Height [m]', ylab='Frequency [Hz]', show_=False)
    plot_xy(xy2[0], xy2[1], 'Gazetas', xlab='Structure Height [m]', ylab='Frequency [Hz]', show_=True)

#freq_Pd()

def PLR_Pd():
    xy1 = param_analysis(data, 's_str_h', 'PLR',
                        discarded=['Abq f_n', 'Gaz. f_n'],
                        needed=[('s_id', 'Ch_Ph35_Pd6_SE175_Sd400')])
    plot_xy(xy1[0], xy1[1], 'G_soil=70Mpa', xlab='Structure Height [m]', ylab='PLR', show_=True)

#PLR_Pd()

''' ---- Soil displacement ---- '''

for i in range(1,4,1):
    #plot_soil_u(filenames[-i])
    pass

#plot_soil_u('2018_6_13--21_1_762000')

for filename in filenames:
    #show_graphics(filename)
    pass



def remove_analysis(data, criterias):
    for d in data:
        for crit in criterias:
            if d[crit[0]] == crit[1]:
                mod_path = model_dir + d['name'] + '.txt'
                abq_path = abaqus_dir + d['name'] + '.txt'
                u1_path = abaqus_dir + d['name'] + '_u1.png'
                u2_path = abaqus_dir + d['name'] + '_u2.png'
                print mod_path
                os.remove(mod_path)
                #os.remove(abq_path)
                #os.remove(u1_path)
                #os.remove(u2_path)
                break

#remove_analysis(data, [('name', '2018_6_10--22_5_978000')])
#remove_analysis(data, [('s_id', 'Sd_Ph35_Pd6_Pt0_Ch80_SE50')])
