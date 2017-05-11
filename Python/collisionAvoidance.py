#Christopher Larson
#collisionAvoidance.py
#Collision-Avoiding Remote-Controlled Car

#Determine when to avoid objects in direct path.
#Does not normally command car unless multiple commands need to be done.
#autonomous.py takes care of the controlling of the car

import time 
import random
from turn import Turn

def CollisionAvoidance(sensorData, ser, car, started):
  rand = random.randint(0,1)
  leftRightAccel, forwardReverseAccel, upDownAccel = car.getAccel()
  leftRightOrient, forwardReverseOrient, upDownOrient = car.getOrientation()
  
  #if the car is not moving, then reverse
  #***This causes issues when the car has to stop...
  #***Needs refactoring
  #if forwardReverseAccel < 0.1:
    #if started:
      #print 'Too close to turn...'
      #print 'Reversing...'
      #return 'Reverse'
  
  #if the car is lifted off the ground, then reverse.
  if leftRightOrient != 0 or forwardReverseOrient != 0:
    if leftRightOrient == 1:
      car.setTurn(45)
    elif leftRightOrient == -1:
      car.setTurn(135)
    print 'Too close to turn...'
    print 'Reversing...'
    return 'Reverse'    

  #if the car's front sensors read 30cm, then reverse 
  if (int(sensorData[0]) < 30) or (int(sensorData[1]) < 30) or (int(sensorData[2]) < 30):     
    direction = Turn(sensorData, rand)
    if direction == 'Left':
       car.setTurn(135)
    elif direction == 'Right':
       car.setTurn(45)
    print 'Too close to turn...'
    print 'Reversing...'
    return 'Reverse'
  #if the car's front sensors read 50cm, then set the speed and get a direction
  #  to turn to.
  elif int(sensorData[1]) < 50:
    car.setSpeed(110)
    time.sleep(0.05)
    direction = Turn(sensorData, rand)
    return direction
  #if the car's front sensors read 50cm, then set the speed and get a direction
  #  to turn to.
  elif int(sensorData[1]) < 100:
    car.setSpeed(112)
    direction = Turn(sensorData, rand)
    return direction

