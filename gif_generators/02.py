import numpy as np
import gizeh as gz
import moviepy.editor as mpy
import colorsys

fps = 24
W,H = 400,400
D = 10 # duration, in seconds
DIR = "../output/square.gif"

def make_frame(t):
    surface = gz.Surface(W,H)
    # hsl is hue color wheel degree, lightness percent, saturation percent
    hue = t * (100/D) / 100
    color = colorsys.hls_to_rgb(hue, .5, 1)
    print hue
    square = gz.square(l=396, fill=color, xy=(200, 200))
    square.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)#.resize(.5) // filesize is smaller, check that this doesnt loss too much?
clip.write_gif(DIR, fps=fps, fuzz=30, opt="OptimizePlus")
