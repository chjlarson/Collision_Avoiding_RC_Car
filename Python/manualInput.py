#Christopher Larson
#manualInput.py
#Collision-Avoiding Remote-Controlled Car

#This will allow for the manual input of a value for the car

from close import Close
import serial

def ManualInput(ser, car, joystick):
  inputVal = raw_input('Enter an integer between -180 and 180 or close to end connection: ')
  if str(inputVal) == 'close':
    Close(ser)
    print('The connection has been closed successfully')
  elif inputVal.lstrip('-').isdigit()== False:
    print('The value entered is not valid. Please Try again.')
  elif int(inputVal) > -181 and int(inputVal) < 181:
    print(inputVal)
    ser.write(inputVal + "\n")
  return

