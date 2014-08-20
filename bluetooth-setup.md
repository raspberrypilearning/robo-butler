#How to set up Bluetooth on your Raspberry Pi
Bluetooth connectivity can be used to transfer files and for communication but it also lets you use game controllers such at the Nintendo Wiimote and the PS3 controller for robotics.

You will need a Bluetooth dongle. Not all adapters work on the Pi - we can't specifically recommend any but we can say that the Inateck Bluetooth 4.0 adapter we are using works really well :).

##Step 1. Connect the dongle and install software
- Plug the dongle into a USB port on your Pi and boot it up.
- At the command line type type `sudo apt-get install --no-install-recommends bluetooth`
- Once the software is installed, type `sudo service bluetooth status`

You should see: `bluetooth is running`. If not, reboot and try again
##Step 2. Test the dongle
Type `hcitool scan`

Any Bluetooth discoverable devices in the area will appear on screen and you are ready to use Bluetooth on the Raspberry Pi.
 
If you don't see anything make sure that you have a phone or other Bluetooth enabled device near to the Pi and discoverable.

