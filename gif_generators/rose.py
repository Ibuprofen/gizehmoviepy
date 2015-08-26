import numpy as np
import gizeh as gz
import moviepy.editor as mpy

# we halve it later
W,H = 400,400
fps=60
D = 2 # duration, in seconds
ncircles = 10
DIR = "./output/rose.webm"

def make_frame(t):
    surface = gz.Surface(W,H)
    for angle in np.linspace(0,2*np.pi,ncircles+1)[:-1]:
        center = np.array([W/2,H/2]) + gz.polar2cart(.2*W,angle)
        for i in [0,1]: # two circles belongin to two groups
            circle = gz.circle(W*.45*(i+t/D),xy=center,
                                  fill=(1,1,1,1.0/255))
            circle.draw(surface)
    return 255*((surface.get_npimage()+1) % 2)

clip = mpy.VideoClip(make_frame, duration=D)
clip.write_videofile(DIR, fps=fps)#, fuzz=30, opt="OptimizePlus")
