#!/usr/bin/python

import sys, getopt
import ledcontroller


def main(argv):
   cmd = ''
   value = ''
   led = ledcontroller.LedController("192.168.0.139")
   try:
      opts, args = getopt.getopt(argv,"hc:v:",["cmd=","value="])
   except getopt.GetoptError:
      print 'lights.py -c <command> -v <value>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'lights.py -c <command> -v <value>'
         sys.exit()
      elif opt in ("-c", "--cmd"):
         cmd = arg
      elif opt in ("-v", "--value"):
         value = arg
   print 'Command is :', cmd
   print 'Value is :', value
   led.set_group_type(1,'rgbw')
   if cmd == 'on' and value == 'white':
       led.on()
       led.set_color('white')
   if cmd == 'on' and value == 'red':
       led.on()
       led.set_color('red')
   if cmd == 'on' and value == 'green':
       led.on()
       led.set_color('green')
   if cmd == 'on' and value == 'blue':
       led.on()
       led.set_color('royal_blue')
   if cmd == 'off':
       led.set_color('white')
       led.off()
   if cmd == 'dim':
       led.set_brightness(int(value))       


if __name__ == "__main__":
   main(sys.argv[1:])
