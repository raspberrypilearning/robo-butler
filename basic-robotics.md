#Basic robotics with the Rasberry Pi
Robotics is one of the simplest ways to start physical computing on the Raspberry Pi. At the other extreme it is one of the most complex topics in computing and engineering, so there's lots of scope for tinkering, hacking and learning to code and build. Most of all, it's great fun!

To make a simple robot you need:

- a robot chassis ie something to fix motors to so that it moves and does stuff
- motors to make the robot move
- a motor controller
- an input device to control the bot 
- a power source for the robot and the Pi

[simple diagram of setup -- Fritizing]

You can buy all of the parts separately, though in some of our beginners' guides we use a pre-built chassis to keep things simpl. Each of our robotics guides will tell you what parts you need.

##A note on motor controllers
**Warning:** Do *not* connect motors directly to your Raspberry Pi! 

All connections should be through a motor controller because if you connect anything other than a tiny motor directly to your Raspberry Pi it will probably damage it. The motor controller uses a separate power supply to power the motors and the Raspberry Pi sends commands to the controller. Motor controllers range from simple controllers for a pound or so to more complex boards that are obviously a lot more capable and flexible. Expect to pay from £8 to £50 for a motor control board.



