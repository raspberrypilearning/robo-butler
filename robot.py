#!/usr/bin/python
#based on Matt Hawkins' code http://www.raspberrypi-spy.co.uk/?p=1101

import cwiid
import time
import RPi.GPIO as io

io.setmode(io.BCM)
pins = (17,18,22,23)
for i in pins:
  io.setup(i,io.OUT)

for i in pins:
  io.output(i,False)

button_delay = 0.1

print 'Press 1 + 2 on your Wii Remote now ...'
time.sleep(1)

# Try to connect to the Wiimote & quit if not found
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Can't connect to Wiimote"
  quit()

print 'Wiimote connected'
wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']
  
  if (buttons & cwiid.BTN_LEFT):
    time.sleep(button_delay)         
    io.output(17, True)
   
  else:
    io.output(17, False)
   
  if(buttons & cwiid.BTN_RIGHT):
    time.sleep(button_delay)          
    io.output(18, True)
    
  else:
    io.output(18, False)
    
  if (buttons & cwiid.BTN_UP):
    time.sleep(button_delay)          
    io.output(22, True)

  else:
    io.output(22, False)
    
  if (buttons & cwiid.BTN_DOWN):
    time.sleep(button_delay)  
    io.output(23, True)

  else:
    io.output(23, False)
    
#press button A to stop all motors
  if (buttons & cwiid.BTN_A):
    time.sleep(button_delay)          
    for i in pins:
      io.output(i, False)    

