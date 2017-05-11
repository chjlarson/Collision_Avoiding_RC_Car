


# Collision_Avoiding_RC_Car

## DETAILS: ##
This was my senior capstone I did while I was getting my BSCS.

> This project had two main parts. The initial part of the project was
> to program a remote-controlled car to be controlled by a variety of
> controllers. The second part of the project was to program the
> remote-controlled car with a basic collision-avoidance algorithm. This
> algorithm utilized the surrounding environmental information to
> determine a suitable course of action without the need for human
> input. Both of these goals were achieved by utilizing an Arduino Uno
> and a Raspberry Pi to communicate with both each other and the
> hardware components of the remote-controlled car.

  
## ORIGINAL PARTS LIST: ##

 - Red Cat Racing 1/10 Volcano Racing truck
 - Raspberry Pi 2
 - Arduino Uno   
 - Raspberry Pi SenseHAT
 - Step-down module
 - Ultrasonic sensors
 - Webcam
 - Bluetooth Adapter
 - Wi-Fi Adapter
 - Breadboard
 - Wiring

**NOTE:** Avoided soldering to allow for modularity of the components for future improvements.  

## Files ##
  **Python Files:**
 - _init_.py
 - arduinoConnect.py
 - autonomous.py
 - bluetoothConnect.py
 - car.py
 - carLauncher.py
 - close.py
 - collsionAvoidance.py
 - manualInput.py
 - ps3Controller.py
 - testCar.py
 - turn.py

**Shell Script Files:**
 - carLauncher.sh
 - checkwifi.sh
 - webLauncher.sh

**Webpage:**
 - Live_Stream.html
 
**Arduino file:**
 - Motor_Servo_Control.ino

## FUTURE IMPROVEMENTS: ##
 - Optimize code
 - Ultrasonic sensor rate of capture change depending on speed. 
	 - *Helps with power management
 - Use ultrasonic sensors in the rear to improve reversing.
 - Facial/object-recognition software with the webcam:
	 - Improve collision avoidance
	 - Create "follow the object" mode
 - Additional Controllers:
	 - Voice controls
	 - Web Controls
    
## CHANGE LOG: ##
 - Replaced Raspberry Pi 2 with Raspberry Pi 3
 - Removed Wi-Fi Adapter and Bluetooth Adapter - Integrated into Raspberry Pi 3
