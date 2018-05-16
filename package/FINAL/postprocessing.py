import json
from pprint import pprint
import os, glob
from moviepy.editor import VideoFileClip
from PIL import Image
import pyglet
import frequency

results_dir = 'results/objects/'

filenames = sorted([os.path.basename(x) for x in glob.glob(results_dir + '2018_5_15--17*')])

def show_result(filename):

    print filename
    with open(results_dir + filename, 'r') as f:

        objects = json.load(f)
        l = len(objects)
        [steel, soil, tube, super_str, pile, sdof] = objects[:6]
        if l > 5:
            num_system = objects[l - 1]
            print num_system['contact_col_soil']

        print('super structure height :' + str(super_str['h']))
        print('Gazetas frequency : ' + str(sdof['f_n']))

    abaqus = 'results/' + filename
    if os.path.isfile(abaqus + '.txt'):
        frequency.plot_results(abaqus + '.txt')

    if os.path.isfile(abaqus + '.mov') or os.path.isfile(abaqus + '.gif'):
        if not os.path.isfile(abaqus + '.gif'):
            #create gif if not exists
            VideoFileClip('results/' + filename + '.mov').write_gif(abaqus + '.gif')
            os.remove('results/' + filename + '.mov')
        show_gif(abaqus + '.gif')
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

for filename in filenames:
    show_result(filename)
