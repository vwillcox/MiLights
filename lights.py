#!/usr/bin/env python
#######################################################################
#                 MiLight Python Script                               # 
#---------------------------------------------------------------------#
#   Control your Milight Compatible lights using python               #
#---------------------------------------------------------------------#
#   V1.0 - Initial                                                    #
#   V2.0 - Add Zone option to control individual devices              #
#   Initial Version - Phil Willis                                     #
#   Version 2.0 - Additions by Vincent Willcox                        #
#---------------------------------------------------------------------#
#   Usage:                                                            #
#   python lights.py -c on -v white -z all                            #
#      Turn on all zones to white                                     #
#   python lights.py -c on -v pink -z 1                               #
#      Turn on zone 1 lights to pink                                  #
#   python lights.py -c dim -v 50 -z 2                                #
#      Turn zone 2 lights to 50% brightness                           #
#######################################################################

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
         try:
            value = int(arg)
         except ValueError:
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
   if cmd == 'off':
       led.set_color('white', zone)
       led.off(zone)
   if cmd == 'dim':
       if zone == None:
          led.set_brightness(int(value))       
       else:
          led.set_brightness(int(value), zone)
   if cmd == 'on':
      led.on(zone)
      led.set_color(value, zone)
   if cmd == 'disco':
      led.on(zone)
      led.disco(zone)
   if cmd == 'disco_faster':
      led.on(zone)
      led.disco_faster(zone)
if __name__ == "__main__":
   main(sys.argv[1:])
