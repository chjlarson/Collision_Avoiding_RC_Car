#Christopher Larson
#autonomous.py
#Collision-Avoiding Remote-Controlled Car

#Allow the car to self-govern itself and perform collision avoidance manuevers.
import time
import random
from close import Close
from car import Car
from collisionAvoidance import CollisionAvoidance
from bluetoothConnect import BluetoothConnect
import pygame

def Autonomous(ser, car, joystick):
  try:    
    print('Please wait while the system initiates')
    #The sensors take a few seconds to get accurate readings.
    #To be safe and allow time to switch input devices, the car will
    #  drive using the autonomous script after 30 seconds from initialization.
    timeout = time.time() + 30
    stopped = False
    reversingTime = time.time() + 4
    stoppingTime = time.time() + 1
    delay = time.time() + 2 
    started = False 

    #While the connection to the Arduino is still present.
    while ser.isOpen():

     #Give the option to partially control the rcar from the keyboard.
     #The autonomous script will still run, but minor changes in speed
     #  and direction can be made.
     #A failsafe 
     try:
      events = pygame.event.get()
      for event in events:
 
        #If the program exits, close the pygame window and enter manual control..
        if event.type == pygame.QUIT:
          return False

        #Partial manual keyboard controls.
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            car.setTurn(45)
          elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            car.setTurn(135)
          elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            car.setTurn(90)
          elif event.key == pygame.K_w:
            car.setSpeed(90)
            pygame.time.delay(10)
            car.setSpeed(102)
          elif event.key == pygame.K_s:
            car.setSpeed(90)
            pygame.time.delay(10)  
            car.setSpeed(60)
 
          #To switch to strictly manual controls.
          elif event.key == pygame.K_m or event.key == pygame.K_ESCAPE:
            car.setSpeed(90)
            car.setTurn(90)
            pygame.quit()
            return False

        #if you turn a controller on and press the "PS" button
        elif event.type == pygame.JOYBUTTONDOWN:
          if joystick.get_button(16) == 1:
            print 'PS button pressed!'
            return True
          
      #************** Beginning of autonomous script ***************
      #Collect Data from the sensors
      #If all of the sensors are ready and are outputting good data,
      #  begin driving.
      sensorData = car.getDistance(ser)
      if (len(sensorData) != 5):
        time.sleep(0.5)
      else:
        for s in range(len(sensorData)):
          if str(sensorData[s]) == '':
             time.sleep(0.25)
        if time.time() > timeout:
          #Send sensor data to the is program to determine course of action.
          control = CollisionAvoidance(sensorData, ser, car, started)
          started = True
          print sensorData
          
          #CollisionAvoidance returns
          if control == 'STOP':
            car.setSpeed(90)
            if time.time() > stoppingTime:
              car.setSpeed(90)
              car.setSpeed(60)
              car.setSpeed(90)
              stopped = True
              stoppingTime = time.time() + 1
          elif control == 'Reverse':
            if stopped == False:
              car.setSpeed(90)
              stopped = True
            if time.time() > stoppingTime:
              car.setSpeed(60)
              stopped = False
              stoppingTime = time.time() + 1
              if time.time() > reversingTime:
                reversingTime = time.time() + 2
          elif control == 'Right':
            car.setTurn(135)
          elif control == 'Left':
            car.setTurn(45)
          else:
            #If nothing of concern in the area, explore the area.
            randSpeed = random.randint(0,5)
            randDirection = random.randint(0,8)
                 
            if time.time() > delay:
              delay = time.time() + 2
              if randSpeed == 0:
                car.setSpeed(90)
              elif randSpeed == 1:
                car.setSpeed(110)
              elif randSpeed == 2:
                car.setSpeed(110)
              elif randSpeed == 3:
                car.setSpeed(112)
              elif randSpeed == 4:
                car.setSpeed(115)

              if randDirection == 0:
                car.setTurn(22)
              elif randDirection == 1:
                car.setTurn(45)
              elif randDirection == 2:
                car.setTurn(68)
              elif randDirection == 3:
                car.setTurn(90)
              elif randDirection == 4:
                car.setTurn(102)
              elif randDirection == 5:
                car.setTurn(125)
              elif randDirection == 6:
                car.setTurn(168)
              elif randDirection == 7:
                car.setTurn(179)
            
     except KeyboardInterrupt:
       print '\nSwitching to Manual input...\n'
       return False
    return

  except KeyboardInterrupt:
    print ('\nSwitching to Manual input...\n')
    return False
