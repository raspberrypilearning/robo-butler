#How to connect a Wiimote to your Raspberry Pi

You should first have Bluetooth up and running on the Pi. See the [Bluetooth set up] guide if you have not done this.

##Step 1. Test that the Bluetooth dongle can see the Wiimote

> **NOTE!** Just because the Bluetooth service is running and can see other devices does not mean that the dongle will be able to see the Wiimote. You may also have problems if you are using a third-party Wiimote instead of an official one. There are no hard and fast rules; you may have to try different configurations if you have problems. 

Type `hcitool scan` and then press the '1' and '2' buttons on your Wiimote at the same time. The blue LEDs should flash on the Wiimote and you should see something like this on screen:
	
> Scanning ...
>          00:1E:02:8A:CD:A1       Nintendo RVL-CNT-01

You may also see other Bluetooth devices that are in range, but you can ignore them.

Now you know that Bluetooth is working and can communicate with the Wiimote. The last step is to make sure that we can talk to the Wiimote using Python.

##Step 2. Install the CWiid Module so that Python can talk to the Wiimote

Type `sudo apt-get install python-cwiid`.

##Step 3. Test it

The following program will test that the Wiimote can communicate with your Raspberry Pi. 
At the command line type `nano wii_remote_1.py` then type in or copy and paste the [code](wii_remote_1.py.py) here:

When you have finished:

- Press `CTRL-o` and then `Enter` to save
- Press `CTRL-x` to exit to the command line

Now run the test program with `sudo python wii_remote_1.py`. Follow the prompts and you should see screen responses to all of your button presses.


[Bluetooth set up]: bluetooth-setup.md
