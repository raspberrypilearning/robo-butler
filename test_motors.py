import RPi.GPIO as io
import time

io.setmode(io.BCM)
pins = [17, 18, 22, 23]
for i in pins:
  io.setup(i, io.output)

#test motors by spinning each one way then the other with 0.5 sec delay
for i in pins:
  print ('Testing pin ' + str(i))
  io.output(i, 1)
  time.sleep(0.5)
  io.output(i, 0)