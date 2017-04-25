#Christopher Larson
#car.py
#Collision-Avoiding Remote-Controlled Car

#This is the Car class that is used to get information about the car

from sense_hat import SenseHat
from arduinoConnect import ArduinoConnect
import serial

ser = ArduinoConnect()
sense = SenseHat()

#Car class
class Car(object):
  def __init__(self, name):
    self.name = name
   
  #Get Distance from Ultra Sonic sensors
  def getDistance(self, ser):
    sensorData = ((str(ser.readline().encode('string-escape'))).split('\\r\\n')[0]).split('-')
    return sensorData

  #Get acceleration from Sense HAT
  #float values
  #0.0*** indicate no movement
  #0.1 > indicates movement
  def getAccel(self):
    acceleration = sense.get_accelerometer_raw()
    leftRight = acceleration['x']
    forwardReverse = acceleration['y']
    upDown = acceleration['z']
    return leftRight, forwardReverse, upDown

  #Get orientation from Sense HAT
  #return x, y, z
  #  x = leftRight, y = forwardReverse, z = upDown
  #  upDown will be 1 for upright or -1 for upsidedown
  def getOrientation(self):
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    if x < 0.15 and x > 0:
      x=0
    elif x > 0.15:
      x=1
    elif x < 0 and x > -0.15:
      x=0
    else:
      x=-1

    if y < 0.15 and y > 0:
      y=0
    elif y > 0.15:
      y=1
    elif y < 0 and y > -0.15:
      y=0
    else:
      y=-1

    if z < 0.15 and z > 0:
      z=0
    elif z > 0.15:
      z=1
    elif z < 0 and z > -0.15:
      z=0
    else:
      z=-1

    return x, y, z

  #Set the Turn angle (0 - 180)
  def setTurn(self, angle):
    self.angle = angle
    ser.write('-' + str(angle) + '\n')
    return

  #Set the speed of the car (0 - 180)
  def setSpeed(self, speed):
    self.speed = speed
    ser.write(str(speed) + '\n')
    return
    
