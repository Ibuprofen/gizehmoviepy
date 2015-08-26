import numpy as np
import gizeh as gz
import moviepy.editor as mpy
import colorsys
from PIL import Image, ImageDraw

gray = (200, 200, 200)
black = (0,0,0)
lightblue = (225, 255, 255)
darkblue = (185, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

fps = 30
W,H = 400,400
D = 3 # duration, in seconds
DIR = "./output/04_rgb_vertical_lines.gif"

def make_frame(t):

  #print t

  img = Image.new("RGBA", (W,H), (255,255,255))

  draw = ImageDraw.Draw(img)


  if t / D > .6:
    lastcolor = red
  elif t / D > .3:
    lastcolor = green
  else:
    lastcolor = black

  for i in range(0, 401, 10):

    if lastcolor == red:
      fillcolor = green
    elif lastcolor == green:
      fillcolor = blue
    elif lastcolor == blue:
      fillcolor = red
    else:
      fillcolor = red

    draw.line([(i, 0), (i, 399)], fill=fillcolor, width=10)

    lastcolor = fillcolor

  #return surface.get_npimage()
  return np.array(img)

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_gif(DIR, fps=fps, fuzz=30, opt="OptimizePlus")
