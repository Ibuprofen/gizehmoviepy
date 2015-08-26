import json
import os.path
from subprocess import call

with open('./config/animations.json') as data_file:
  data = json.load(data_file)


#-crf values can go from 4 to 63. Lower values mean better quality.
#-b:v is the maximum allowed bitrate. Higher means better quality.
#-vf scale=640:-1 sets the width to 640px. The height will be calculated automatically according to the aspect ratio of the input.
#-r forces fps

# ffmpeg -i ./web/gifs/blah.gif -c:v libvpx -crf 4 -b:v 1M -vf scale=400:400 -r 30 -y ./blah.webm

for anim in data:
  print "./web/webm/" + anim["id"] + ".webm"
  call(["ffmpeg",
    "-i", "./web/gifs/" + anim["id"] + ".gif",
    "-c:v", "libvpx",
    "-crf", "4",
    "-b:v", "1M",
    "-vf", "scale=400:400",
    "-r", "30",
    "-y",
    "./web/webm/" + anim["id"] + ".webm"])

