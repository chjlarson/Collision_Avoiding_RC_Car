#Christopher Larson
#arduinoConnect
#Collision-Avoiding Remote-Controlled Car

#This will attempt to connect to the arduino.
import serial
import sys

def ArduinoConnect():
#initialize the connection to the arduino
  ser = serial.Serial(
  port = '/dev/ttyACM0',
  baudrate = 9600,
  timeout=999
  )
#test the connection to the arduino
#only open port if the port is not already open
  try:
    if (ser.isOpen() == False):
      ser.open()
    return ser
  except Exception, e:
    print('Error: could not open serial port' + str(e))
    exit()
