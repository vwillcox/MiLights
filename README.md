# MiLights

I could not get HaBridge to reliably send commands to a MiLight controller so I created a small application to ensure the commands were sent.

Builds on top of ledcontroller and ha bridge to allow control of MiLights from the command line.

LedController can be found here: https://github.com/ojarva/python-ledcontroller

And Ha Bridge found here: https://github.com/bwssytems/ha-bridge

Usage:

    lights.py -c command -v value

command is:

    on
    dim
    off
  
value is:
 
  When used with <b>on</b> is one of white, red, green, blue
 
  When used with <b>dim</b> is a number between 0 and 100
 
  When used with <b>off</b> is not used
 
 
 
