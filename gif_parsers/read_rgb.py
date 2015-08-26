import json
from PIL import Image
import collections

with open('../config/nodes.json') as data_file:
    nodes = json.load(data_file)

# empty fucker
ordered_nodes = [None] * len(nodes)

# populate fucker
for i, pos in nodes.items():
  ordered_nodes[int(i)] = [pos['x'], pos['y']]

filename = "04_rgb_vertical_lines"

im = Image.open("../gif_generators/output/"+filename+".gif") #Can be many different formats.

target_size = 400, 400

resize = False
if target_size != im.size:
  resize = True

data = []

# To iterate through the entire gif
try:
  frame_num = 0
  while True:
    im.seek(frame_num)

    frame_data = []

    # do something to im
    img = im.convert('RGB')

    if resize == True:
      print "Resizing"
      img.thumbnail(target_size, Image.ANTIALIAS)

    for x, y in ordered_nodes:
      frame_data.append(img.getpixel((x, y)))

    #print r, g, b
    data.append(frame_data)

    # write to json

    print frame_num
    frame_num+=1
except EOFError:
    pass # end of sequence

#print data

#print r, g, b

with open(filename+'.json', 'w') as outfile:
    json.dump({
      "meta": {},
      "data": data
    }, outfile)


print im.size #Get the width and hight of the image for iterating over
#print pix[,y] #Get the RGBA Value of the a pixel of an image
