#!/usr/bin/python

import sys, getopt
import ledcontroller


def main(argv):
   cmd = ''
   value = ''
   zone = ''
   led = ledcontroller.LedController("192.168.0.150")
   try:
      opts, args = getopt.getopt(argv,"hc:v:z:",["cmd=","value=","zone="])
   except getopt.GetoptError:
      print 'lights.py -c <command> -v <value> -z <value>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'lights.py -c <command> -v <value> -z <value>'
         sys.exit()
      elif opt in ("-c", "--cmd"):
         cmd = arg
      elif opt in ("-v", "--value"):
         value = arg
      elif opt in ("-z", "--zone"):
         try:
            zone = int(arg)
         except ValueError:
            zone = None
   print 'Command is :', cmd
   print 'Value is :', value
   print 'Zone is :', zone
   led.set_group_type(1,'rgbw')
   if cmd == 'on' and value == 'white':
       led.on(zone)
       led.set_color('white', zone)
   if cmd == 'on' and value == 'red':
       led.on(zone)
       led.set_color('red', zone)
   if cmd == 'on' and value == 'green':
       led.on(zone)
       led.set_color('green', zone)
   if cmd == 'on' and value == 'blue':
       led.on(zone)
       led.set_color('royal_blue', zone)
   if cmd == 'off':
       led.set_color('white', zone)
       led.off(zone)
   if cmd == 'dim':
       if zone == None:
          led.set_brightness(int(value))       
       else:
          led.set_brightness(int(value), zone)

if __name__ == "__main__":
   main(sys.argv[1:])
