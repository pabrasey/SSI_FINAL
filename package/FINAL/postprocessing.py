import json
import os, glob
from collections import OrderedDict
from moviepy.editor import VideoFileClip
from prettytable import PrettyTable
import decimal
import pyglet
import frequency


def show_table(data):

    t = PrettyTable(data[0].keys())
    for row in data:
        t.add_row(row.values())
    print t


def get_data(filenames):
    data = []
    for filename in filenames:
        # model data
        with open(model_dir + filename + '.txt', 'r') as f:  # model
            objects = json.load(f, parse_float=lambda s: decimal.Decimal(str(round(float(s), 4))))
            l = len(objects)
            [steel, soil, tube, super_str, pile, sdof] = objects[:6]
            if not 'pile_active_l' in sdof: sdof['pile_active_l'] = 'NaN'
        dic = OrderedDict([
            ('name'      ,   filename),
            ('s_str_h'   ,   super_str['h']),
            ('pile depth',   pile['h']),
            ('pile_act_l',   sdof['pile_active_l']),
            ('r_e'       ,   tube['r_e']),
            ('t'         ,   tube['t']),
            ('Gaz. f_n'  ,   sdof['f_n']),
        ])

        # abaqus results

        abq_res = get_abq_data(filename)
        if len(data) > 0:
            f_n = abq_res['freq'][0][1]
            top_disp_1 = abq_res['top_disp_1']
            n_sys = objects[l - 1]

            dic.update([
                ('Abq f_n'   ,   f_n),
                ('contact'   ,   n_sys['contact_col_soil']),
                ('phi'       ,   soil['phi']),
                ('soil depth',   n_sys['soil_depth']),
                ('soil width',   n_sys['soil_diameter']),
                ('soil_mesh' ,   n_sys['soil_mesh_size']),
                ('fix_sides' ,   n_sys['fixed_sides'])
            ])
        else:
            dic.update([
                ('Abq f_n',      'NaN'),
                ('contact',      'NaN'),
                ('phi',          'NaN'),
                ('soil depth',   'NaN'),
                ('soil width',   'NaN'),
                ('soil_mesh',    'NaN'),
                ('fix_sides',    'NaN'),
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


def show_graphics(filename):

    print filename
    top_disp_1 = get_abq_data(filename)['top_disp_1']
    frequency.plot_results(top_disp_1[0], top_disp_1[1])

    abq_basename = abaqus_dir + filename

    if os.path.isfile(abq_basename + '.mov') or os.path.isfile(abq_basename + '.gif'):
        if not os.path.isfile(abq_basename + '.gif'):
            #create gif if doesn't exists
            VideoFileClip(abq_basename + '.mov').write_gif(abq_basename + '.gif')
            os.remove(abq_basename + '.mov')
        #show_gif(abq_basename + '.gif')

    print ''


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

model_dir = 'results/models/'
abaqus_dir = 'results/abaqus/'

filenames = sorted([os.path.basename(os.path.splitext(x)[0]) for x in glob.glob(model_dir + '2018_5_*')])

data = get_data(filenames)
show_table(data)

for filename in filenames:
    #show_graphics(filename)
    pass
