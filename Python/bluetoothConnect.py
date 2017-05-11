#Christopher Larson
#bluetoothConnect.py
#Collision-Avoiding Remote-Controlled Car

#This will attempt to connect to a bluetooth controller and 
#return whether Pygame quit because of the lack of a controller present.

import pygame
from close import Close

def BluetoothConnect(ser):

  if ser.isOpen():
    #clean house before beginning
    try:
      ser.flushInput()
      ser.flushOutput()

      #initiate pygame
      pygame.init()
      pygame.display.init()
      pygame.display.set_mode()
      pygame.joystick.init()
      

      #initialize the joystick
      #or if not present, close pygame
      if pygame.joystick.get_count() != 0:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

      else:
        joystick = 0
        
      return joystick

    
    except IOError as e:
      print('I/O error ({0}: {1}'.format(e.errno,e.strerror))
      print('Could not connect')
  else:
    print('Error: Cannot open serial port ')
