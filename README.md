# RComp
Drone software repo

Connecting to the Raspberry Pi 5 without a screen:
  1. Using SSH: Headless
     a) Connect your laptop to IEEE WiFi. If in the field, then things get complicated.
     b) Make sure the Raspberry Pi is powered on and give it some time to boot up.
     c) Open PowerShell on your laptop.
     d) Type "ssh username@hostname" (Not sure what the username and hostname are for the UAV yet)
     e) You will be prompted for a password. Type in the password for the UAV.
     f) If the password is correct, you should have a remote shell.
     
  3. Using VNC: Remote Desktop
     a) Install a VNC client on your computer
     b) Make sure VNC is enabled on the raspberry pi using raspi-config.
     c) Make sure both your computer and the Raspberry pi are powered on and connected to the same network.
     d) Open the VNC client on your computer and connect to the Raspberry Pi using its IP address or hostname.

 Note: SSH and VNC are not enabled by default. You need to choose the options either when using raspi imager when writing the SD card or use raspi-config to enable them after.
