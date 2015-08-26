import json
import os.path
from subprocess import call

with open('./config/animations.json') as data_file:
  data = json.load(data_file)


# download them
for anim in data:
  if os.path.isfile("./web/gifs/" + anim["id"] + ".gif"):
    print anim["id"] + " already exists"
  else:
    call(["wget", anim["source"], "-O", "./web/gifs/" + anim["id"] + ".gif"])
