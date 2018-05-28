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
import frequency


def show_table(data):

    t = PrettyTable(data[0].keys())
    for row in data:
        t.add_row(row.values())
    print(t)


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
            ('name'      ,   filename[7:-4]),
            ('s_id'      ,   lysis['serie_id']),
            ('s_str_h'   ,   super_str['h']),
            ('pile_depth',   pile['h']),
            ('pile_act_l',   sdof['pile_active_l']),
            ('r_e'       ,   tube['r_e']),
            ('t'         ,   tube['t']),
            ('Gaz. f_n'  ,   sdof['f_n']),
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
                soilU_ratio = "%.3f" % (soil_u[dof][1][-1] / soil_u[dof][1][0])
            else:
                dof = -1
                soilU_ratio = 'NaN'

            dic.update([
                ('Abq f_n'   ,   f_n),
                ('contact'   ,   n_sys['contact_col_soil']),
                ('phi'       ,   soil['phi']),
                ('soil_depth',   n_sys['soil_depth']),
                ('soil_width',   n_sys['soil_diameter']),
                ('soil_mesh' ,   n_sys['soil_mesh_size']),
                ('fix_sides' ,   n_sys['fixed_sides']),
                ('soilU_oi'  ,   soilU_ratio),
                ('dir'       ,   dof + 1 ),
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
                ('soilU_oi',    'NaN'),
                ('dir',          'NaN'),
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
    plot_xy(soil_u1[0], soil_u1[1], 'U1', 'x [m] (path)', 'U [m]', False)
    soil_u2 = abq_res['soil_u2']
    plot_xy(soil_u2[0], soil_u2[1], 'U2', 'x [m] (path)', 'U [m]', False)
    soil_u3 = abq_res['soil_u3']
    plot_xy(soil_u3[0], soil_u3[1], 'U3', 'x [m] (path)', 'U [m]', True)



def plot_xy(x, y, label, xlab, ylab, show_):
    plot(x, y, label=label)
    if show_:
        legend(framealpha=1, frameon=False);
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


def param_analysis(data, x, y, discarded, needed):
    full_data = copy.deepcopy(data)
    data = copy.deepcopy(data)

    # remove the x, y and discarded keys in data
    for d in data:
        del d[x], d[y], d['name']
        for disc in discarded:
            del d[disc]

    # get the duplicates
    dupe_ind = [n for n, e in enumerate(data) if e in data[:n]]

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


model_dir = 'results/models/'
abaqus_dir = 'results/abaqus/'

filenames = sorted([os.path.basename(os.path.splitext(x)[0]) for x in glob.glob(model_dir + '2018_5_*')])
filenames.sort(key=lambda x: os.path.getmtime(model_dir + x + '.txt'))

data = get_data(filenames)
show_table(data)

def soil_width_analysis():
    xy1 = param_analysis(data, 'soil_width', 'Abq f_n',
                   ['contact', 'soil_mesh', 'pile_act_l'],
                   [('s_str_h', 80), ('soil_depth', 60), ('fix_sides', True), ])
    xy2 = param_analysis(data, 'soil_width', 'Abq f_n',
                   ['contact', 'soil_mesh', 'pile_act_l'],
                   [('s_str_h', 80), ('soil_depth', 60), ('fix_sides', False), ])


xy3 = param_analysis(data, 'pile_depth', 'soilU_oi',
               ['contact', 'soil_depth', 'pile_act_l', 'Abq f_n'],
               [('s_str_h', 80), ('fix_sides', False), ('s_id', '0')])


plot_xy(xy3[0], xy3[1], 'Ratio In/Out', 'pile_depth', 'soilU_oi', True)

for i in range(1,3,1):
    plot_soil_u(filenames[-i])
    pass

for filename in filenames:
    #show_graphics(filename)
    pass
