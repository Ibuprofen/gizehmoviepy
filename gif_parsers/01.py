import serial
import json
import time

#ser = serial.Serial('/dev/ttyACM0', 9600)

FRAME_DELAY = 0
START_CHAR = '#'
END_CHAR = '$'

last_time = time.time();

#with open('../config/nodes.json') as data_file:
#    data = json.load(data_file)

with open('./data.json') as data_file:
  data = json.load(data_file)

FPS = float(data['meta']['fps'])

print "FPS:", FPS
print "Number of frames:", len(data['data'])
print "Expected duration:", len(data['data']) / FPS, "seconds"

def write_frame(frameArray):
  global last_time

  last_time = time.time()

  str = START_CHAR

  # zero is zero..... we are off by one
  # seriouly put the node address in the json so we can be explicit and know its right
  # it looks like the datatype is a list, is a python list in order, if we do something else do we ruin that freebie?
  # for now, we lie!
  for x, colors in enumerate(frameArray):
                                                  # TODO: that + 1 gonna fuck you up!
    str += "@{0:0>3}{1:0>3}{2:0>3}{3:0>3}".format(x + 1, colors[0], colors[1], colors[2])

  str += END_CHAR

  #print str
  #ser.write(str)


def sleep_it_off():
  global last_time

  new_time = time.time()
  # see how many milliseconds we have to sleep for
  # then divide by 1000.0 since time.sleep() uses seconds
  sleep_time = ((1000.0 / FPS) - (new_time - last_time)) / 1000.0
  if sleep_time > 0:
      time.sleep(sleep_time)
  last_time = new_time


# TODO: do we get the correct ordering for free?
for frame in data['data']:

  write_frame(frame)

  sleep_it_off();

