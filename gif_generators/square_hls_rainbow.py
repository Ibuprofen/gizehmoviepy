import numpy as np
import gizeh as gz
import moviepy.editor as mpy
import colorsys

fps = 60
W,H = 400,400
D = 10 # duration, in seconds
DIR = "./output/square_hls_rainbow.webm"

def make_frame(t):
    surface = gz.Surface(W,H)
    # hsl is hue color wheel degree, lightness percent, saturation percent
    hue = t * (100/D) / 100
    color = colorsys.hls_to_rgb(hue, .5, 1)
    square = gz.square(l=W*2, fill=color, xy=(1, 1))
    square.draw(surface)
    return surface.get_npimage()

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_videofile(DIR, fps=fps);#, fuzz=30, opt="OptimizePlus")
