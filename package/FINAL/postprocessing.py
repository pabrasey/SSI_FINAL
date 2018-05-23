import json
import os, glob
from moviepy.editor import VideoFileClip
from prettytable import PrettyTable
import decimal
import pyglet
import frequency


def show_table(filenames):

    t = PrettyTable(['name', 's_str_h', 'pile depth', 'pile_act_l', 'r_e', 't', 'Gaz. f_n',
                     'Abq f_n', 'contact', 'phi', 'soil depth', 'soil width',
                     'soil_mesh', 'fix_sides'])

    for filename in filenames:
        with open(model_dir + filename, 'r') as f: # model
            objects = json.load(f, parse_float=lambda s: decimal.Decimal(str(round(float(s), 4))))
            l = len(objects)
            [steel, soil, tube, super_str, pile, sdof] = objects[:6]
            if not 'pile_active_l' in sdof: sdof['pile_active_l'] = 'NaN'


            data = get_abq_data(filename)
            if len(data) > 0: # abaqus results

                f_n = data['freq'][0][1]
                top_disp_1 = data['top_disp_1']
                n_sys = objects[l - 1]
                t.add_row([
                    filename, super_str['h'], pile['h'], sdof['pile_active_l'], tube['r_e'], tube['t'], sdof['f_n'],
                     f_n, n_sys['contact_col_soil'], soil['phi'], n_sys['soil_depth'], n_sys['soil_diameter'],
                    n_sys['soil_mesh_size'], n_sys['fixed_sides']
                ])
            else:
                t.add_row(
                    [filename, super_str['h'], pile['h'], sdof['pile_active_l'], tube['r_e'], tube['t'], sdof['f_n'],
                     'NaN', 'NaN', soil['phi'], 'NaN', 'NaN', 'NaN', 'NaN'])
    print t


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

filenames = sorted([os.path.basename(x) for x in glob.glob(model_dir + '2018_5_*')])

show_table(filenames)

for filename in filenames:
    #show_graphics(filename)
    pass
