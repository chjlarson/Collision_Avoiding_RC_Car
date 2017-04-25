#include <NewPing.h>
#include <Servo.h>

//setup NewPing for frontRightSensor,frontSensor,
//frontLeftSensor, backRightSensor, and backLeftSensor
#define SONAR_NUM 5
#define MAX_DISTANCE 200
#define PING_INTERVAL 35
#define DATA_COUNT 2

unsigned long pingTimer[SONAR_NUM];
long duration, distance, frontRightSensor, frontSensor, frontLeftSensor, backRightSensor, backLeftSensor;
unsigned int cm[SONAR_NUM];
int num[SONAR_NUM];
int average[SONAR_NUM];
int count = 0;
String incomingString;
uint8_t currentSensor=0;

NewPing sonar[SONAR_NUM] = {
  NewPing(2,3,MAX_DISTANCE),
  NewPing(4,5,MAX_DISTANCE),
  NewPing(6,7,MAX_DISTANCE),
  NewPing(8,9,MAX_DISTANCE),
  NewPing(A4,A5,MAX_DISTANCE)
};

// Setup for motor and Servo.
Servo myMotor;
Servo myServo;

// Setup for Remote Controller
int ch1;
int ch2;

void setup()
{
  // Motor = Pin 10
  // Servo = Pin 11
  myMotor.attach(10);
  myServo.attach(11);
  
  // Remote Controller Motor Control = A3
  // Remote Controller Motor Control = A0
  pinMode(A3, INPUT);
  pinMode(A0, INPUT);
  
  //Start sensors
  pingTimer[0] = millis();
  for (uint8_t i=1; i<SONAR_NUM;i++)
    pingTimer[i]=pingTimer[i-1]+PING_INTERVAL;
  
  // Required for I/O from Serial monitor
  Serial.begin(9600);

  // Print a startup message
  Serial.println("Initializing...");
  Serial.println("Initializing...");
}


void loop()
{ 
  //determine distance
  for (uint8_t i=0;i<SONAR_NUM;i++){
    if (millis() >= pingTimer[i]){
      pingTimer[i] += PING_INTERVAL * SONAR_NUM;
      if (i == 0 && currentSensor == SONAR_NUM - 1)
        oneSensorCycle();
      sonar[currentSensor].timer_stop();
      currentSensor = i;
      cm[currentSensor] = 0;
      sonar[currentSensor].ping_timer(echoCheck);
    }
  }
  // Set to low frequency to check for controller, but not 
  // disrupt the sensors 
  ch1 = pulseIn(A0, HIGH, 2500);
  ch2 = pulseIn(A3, HIGH, 2500);
  
  if (ch1 == 0)
  {
  
  // If there is incoming value
  if(Serial.available() > 0)
  {
    // read the value
    char endVal = Serial.read();
  
    /*
    *  If endVal isn't a newline (linefeed) character,
    *  then add the character to the incomingString
    */
    if (endVal != 10){
     
      // Add the character to
      // the incomingString
      incomingString += endVal;
    }

    // received a newline (linefeed) character
    // this means we are done making a string
    else
    {
      // Convert the string to an integer
      int inputVal = incomingString.toInt();
    
      /*
      *  Write an integer between -180 and 180. 
      */
      
      if (inputVal > -181 && inputVal < 181)
      {
        // The value is between 0 and 180.
        // Write to motor.
        if (inputVal > 0 && inputVal < 181)
        { 
          myMotor.write(inputVal);
        }
         // The value is between 0 and -180.
         // Write to the servo.
         if (inputVal < 1 && inputVal > -181)
         {
           //Serial.println("Value is between -181 and 0");
           int servoVal = abs(inputVal);
           myServo.write (servoVal);
         }
      }
      else 
      {   
        Serial.println("Value is NOT between -180 and 180");
        Serial.println("Error with the input");
      }
    // Reset the value of the incomingString
    incomingString = "";
    }
  }
  
  }
  else
  {
   // The remote controller is turned on, so increase frequency
   // of radio
   ch1 = pulseIn(A0, HIGH, 25000);
   ch2 = pulseIn(A3, HIGH, 25000);
   Turn();
   Drive(); 
  }
}

// Translating radio controller data into serial input.
void Drive ()
{
 if (ch2 > 1300 && ch2 < 1351)
 {
  myMotor.write(90); 
 }
 else if (ch2 > 1350)
 {
   if (ch2 > 1350 && ch2 < 1451)
   {
     myMotor.write(100); 
   }
   else if (ch2 > 1450 && ch2 < 1576)
   {
     myMotor.write(110); 
   }
   else if (ch2 > 1575 && ch2 < 1701)
   {
     myMotor.write(120); 
   }
   else if (ch2 > 1700 && ch2 < 1751)
   {
     myMotor.write(130); 
   }
 }
 else if (ch2 < 1300 && ch2 > 860)
 {
   if (ch2 > 1176 && ch2 < 1300)
   {
     myMotor.write(80); 
   }
   else if (ch2 > 1051 && ch2 < 1175)
   {
     myMotor.write(70); 
   }
   else if (ch2 > 879 && ch2 < 1050)
   {
     myMotor.write(60); 
   }
 } 
}


void echoCheck ()
{
 if (sonar[currentSensor].check_timer())
   cm[currentSensor] = sonar[currentSensor].ping_result/ US_ROUNDTRIP_CM;
}


void oneSensorCycle() 
{
  //This finds the average of DATA_COUNT of each sonar's echo value
  if (count < DATA_COUNT){
    for (int i = 0; i < SONAR_NUM; i++){
      num[i] = num[i] + cm[i];
    }
    count++;
  }
  else if (count == DATA_COUNT){
    for (int j = 0; j < SONAR_NUM;j++){
    average[j] = num[j]/DATA_COUNT;
      num[j] = 0;
    }  
    count=0;
  }
  
  //This will print out the average of each sonar
  //format: frontRightSensor-frontSensor-frontLeftSensor-backRightSensor-backLeftSensor\n
  for(int k=0;k < SONAR_NUM; k++){
    if (k==SONAR_NUM-1){
      Serial.print(average[k]);
    }
    else{
      Serial.print(average[k]);
      Serial.print("-");
    }
  }
  Serial.println();
}

// This will turn radio controller data into serial input
void Turn()
{
  if (ch1 > 1250 && ch1 < 1400)
 {
  myServo.write(90); 
 }
 else if (ch1 > 1400)
 {
   if (ch1 > 1400 && ch1 < 1501)
   {
     myServo.write(120); 
   }
   else if (ch1 > 1500 && ch1 < 1676)
   {
     myServo.write(150); 
   }
   else if (ch1 > 1675 && ch1 < 1750)
   {
     myServo.write(180); 
   }
 }
 else if (ch1 < 1250 && ch1 > 860)
 {
   if (ch1 > 1176 && ch1 < 1250)
   {
     myServo.write(60); 
   }
   else if (ch1 > 1051 && ch1 < 1175)
   {
     myServo.write(30); 
   }
   else if (ch1 > 869 && ch1 < 1050)
   {
     myServo.write(1); 
   }
 }  
}
