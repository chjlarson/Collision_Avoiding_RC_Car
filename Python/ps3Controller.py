#Christopher Larson

import time
import pygame
from autonomous import Autonomous

# Function to handle pygame events
def EventHandler(events, ser, car, joystick, hadEvent, forward, reverse, left, right, quit, yAxis, yAxisInverted, xAxis, xAxisInverted, interval):    
  # Handle each event individually
  for event in events:
    if event.type == pygame.QUIT:
      # User exit
      hadEvent = True
      quit = True
    elif event.type == pygame.KEYDOWN:
      # A key has been pressed, see if it is one we want
      hadEvent = True
      if event.key == pygame.K_ESCAPE:
        quit = True
    elif event.type == pygame.KEYUP:
      # A key has been released, see if it is one we want
      hadEvent = True
      if event.key == pygame.K_ESCAPE:
        quit = False
    elif event.type == pygame.JOYBUTTONDOWN:
      car.setSpeed(90)
      car.setTurn(90)
      if joystick.get_button(16) == 1:
        quit = True
      elif joystick.get_button(12) == 1:
        Autonomous(ser, car, joystick)
    elif event.type == pygame.JOYAXISMOTION:
      # A joystick has been moved, read axis positions (-1 to +1)
      hadEvent = True
      upDown = joystick.get_axis(yAxis)
      leftRight = joystick.get_axis(xAxis)
      # Invert any axes which are incorrect
      if yAxisInverted:
        upDown = -upDown
      if xAxisInverted:
        leftRight = -leftRight
      # Determine Up / Down values
      if upDown < -0.1:
        forward = True
        reverse = False
      elif upDown > 0.1:
        forward = False
        reverse = True
      else:
        forward = False
        reverse = False
      # Determine Left / Right values
      if leftRight < -0.1:
        left = True
        right = False
      elif leftRight > 0.1:
        left = False
        right = True
      else:
        left = False
        right = False
  return hadEvent, forward, reverse, left, right, quit  

def PS3Controller(ser, car, joystick):
  yAxis = 1                          # Joystick axis to read for up / down position
  yAxisInverted = False              # Set this to True if up and down appear to be swapped
  xAxis = 3                          # Joystick axis to read for left / right position
  xAxisInverted = False              # Set this to True if left and right appear to be swapped
  interval = 0.05                    # Time between keyboard updates in seconds, smaller responds faster but uses more processor time
  hadEvent = True
  forward = False
  reverse = False
  left = False
  right = False
  quit = False
  
  try:
    print 'Press [ESC] to quit'
    # Loop indefinitely
    while True:
      ser.flushInput()
      ser.flushOutput()
      # Get the currently pressed keys on the keyboard
      hadEvent, forward, reverse, left, right, quit = EventHandler(pygame.event.get(), ser, car, joystick, hadEvent, forward, reverse, left, right, quit, yAxis, yAxisInverted, xAxis, xAxisInverted, interval)
      if hadEvent:
        # Keys have changed, generate the command list based on keys
        hadEvent = False
        if quit:
          break
        elif left:
          car.setTurn(45)
        elif right:
          car.setTurn(135)
        elif forward:
          car.setSpeed(110)
        elif reverse:
          car.setSpeed(60)
        else:
          car.setTurn(90)
          car.setSpeed(90)
        # Wait for the interval period
        time.sleep(interval)
    car.setSpeed(90)
    car.setTurn(90)
    pygame.quit()
  except KeyboardInterrupt:
    # CTRL+C exit, disable all drives
    car.setSpeed(90)
    car.setTurn(90)
    pygame.quit()
  return 
