import json
import os, glob
from moviepy.editor import VideoFileClip
from prettytable import PrettyTable
import pyglet
import frequency

results_dir = 'results/objects/'

filenames = sorted([os.path.basename(x) for x in glob.glob(results_dir + '2018_5_17*')])

def show_table(filenames):

    t = PrettyTable(['name', 'super_str.h', 'section r_e', 't', 'Gazetas f_n', 'contact', 'phi'])

    for filename in filenames:
        with open(results_dir + filename, 'r') as f:
            objects = json.load(f)
            l = len(objects)
            [steel, soil, tube, super_str, pile, sdof] = objects[:6]
            if l > 5:
                num_system = objects[l - 1]
                t.add_row(
                    [filename, super_str['h'], tube['r_e'], tube['t'], sdof['f_n'], num_system['contact_col_soil'], soil['phi']])
            else:
                t.add_row(
                    [filename, super_str['h'], tube['r_e'], tube['t'], sdof['f_n'], 'NaN', soil['phi']])
    print t


def show_graphics(filename):

    print filename
    abaqusname = 'results/' + filename
    if os.path.isfile(abaqusname + '.txt'):
        frequency.plot_results(abaqusname + '.txt')
        pass

    if os.path.isfile(abaqusname + '.mov') or os.path.isfile(abaqusname + '.gif'):
        if not os.path.isfile(abaqusname + '.gif'):
            #create gif if doesn't exists
            VideoFileClip('results/' + filename + '.mov').write_gif(abaqusname + '.gif')
            os.remove('results/' + filename + '.mov')
        show_gif(abaqusname + '.gif')

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


show_table(filenames)

for filename in filenames:
    #show_graphics(filename)
    pass
