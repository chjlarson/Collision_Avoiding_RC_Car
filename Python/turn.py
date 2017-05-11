#Christopher Larson
#turn.py
#Collision-Avoiding Remote-Controlled Car

#Determine if and when to turn and in what direction.

def Turn(sensorData, rand):
  if int(sensorData[0]) < 35 and int(sensorData[2]) > 35:
    print 'turning right...'
    return 'Right'
  elif int(sensorData[2]) < 35 and int(sensorData[0]) > 35:
    print 'turning left...'
    return 'Left'
  elif int(sensorData[0]) < 35 and int(sensorData[2]) < 35:
    print 'Both sides obstructed...'
    print 'Picking random side to turn'
    if rand == 0:
      return 'Right'
    else:
      return 'Left'
  return

