#Christopher Larson
#testCar.py
#Collision-Avoiding Remote-Controlled Car

from arduinoConnect import ArduinoConnect
from autonomous import Autonomous
from bluetoothConnect import BluetoothConnect
from car import Car
from ps3Controller import *
import pygame
from manualInput import ManualInput

def main():
  #initialize the connection to the arduino
  ser = ArduinoConnect()
  print 'To control the car manually, please press "m" on the keyboard'
  print 'To control the car with the Remote Controller, then power on the device'
  print 'To control the car with the PS3 Controller, \nplease power on and press the "PS" button\n'

  #Check if there is a PS3 Controller, assume there is not one.   
  car = Car('James')
  joystick = BluetoothConnect(ser)

  try:
    val = Autonomous(ser, car, joystick)
    if val == False:
      while ser.isOpen():
         ManualInput(ser, car, joystick)
    else:
      while ser.isOpen():
        PS3Controller(ser, car, joystick)
  except KeyboardInterrupt:
    print('Switching to manual input...')
    ManualInput(ser, car, joystick)
main()
