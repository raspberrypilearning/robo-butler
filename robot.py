#!/usr/bin/python
#based on Matt Hawkins' code http://www.raspberrypi-spy.co.uk/?p=1101
#Re written by Ryan Walmsley

import cwiid
import time
import RPi.GPIO as io

io.setmode(io.BCM)
#Motor 1 is designed to be the motors on the left, Motor 2 is designed to be on the right
#If one motor is in the wrong direction you can swap the pins around to save you having to re-wrire the robot.
m1a = 17 #Motor 1 Forwards
m1b = 18 #Motor 1 Backwards
m2a = 22 #Motor 2 Forwards
m2b = 23 #Motor 2 Backwards
pins = (m1a,m1b,m2a,m2b)
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
  if (buttons & cwiid.BTN_UP):
    #Forwards
    time.sleep(button_delay)    
    io.output(m1a, True)      
    io.output(m2a, True)
   
  elif (buttons & cwiid.BTN_DOWN):
    time.sleep(button_delay)  
    io.output(m1b, True)
    io.output(m2b, True)
  
  elif (buttons & cwiid.BTN_LEFT):
    time.sleep(button_delay)         
    io.output(m1a, True)
    io.output(m2b, True)
   
  elif(buttons & cwiid.BTN_RIGHT):
    time.sleep(button_delay)          
    io.output(m1b, True)
    io.output(m2a, True)
  
  else:
    io.output(m1a, False)
    io.output(m1b, False)
    io.output(m2a, False)
    io.output(m2b, False)
   

    
#press button A to stop all motors
  if (buttons & cwiid.BTN_A):
    time.sleep(button_delay)          
    for i in pins:
      io.output(i, False)    

