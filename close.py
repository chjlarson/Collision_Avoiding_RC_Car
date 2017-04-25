#Christopher Larson
#close.py
#Collision-Avoiding Remote-Controlled Car

#Stop the car and close the connection.
#Quicker through serial write.
import serial

def Close(ser):
  ser.write('-90'+'\n')
  ser.write('90'+'\n')
  ser.close()
  return

