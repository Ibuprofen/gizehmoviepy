import numpy as np
import gizeh as gz
import moviepy.editor as mpy
import colorsys
from PIL import Image, ImageDraw

fps = 30
W,H = 400,400
D = 10 # duration, in seconds
DIR = "../output/03_img_to_numpy.gif"

def make_frame(t):

    img = Image.new("RGBA", (W,H), (255,255,255))

    draw = ImageDraw.Draw(img)

    hue = t * (100/D) / 100
    #print hue
    color = colorsys.hls_to_rgb(hue, .5, 1)

    #print color
    color = (int(color[0]), int(color[1]), int(color[2]))
    #print color

    draw.rectangle(((1, 1), (img.size[0]-1, img.size[1]-1)), fill=color, outline=None)

    return np.array(img.convert("L"))

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif(DIR, fps=fps, fuzz=30, opt="OptimizePlus")
