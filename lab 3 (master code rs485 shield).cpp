#include <SoftwareSerial.h>
#include<string.h>

int led = 13;
int EN = 2;
int analogPin = A3; //Definition RS485 shield enable terminal (the 2nd digital IO ports),
//high for the sending state, the low level of receiving state
void ReciveModetransmitMode(int state){
    if(state ==1){
        //turn on for tranmitter
        delay(10);
        digitalWrite(EN,HIGH);
    }
    else{
        delay(10);
        digitalWrite(EN,LOW);
    }
}

//software serial
// Set up a new SoftwareSerial object with RX in digital pin 10 and TX in digital pin 11
SoftwareSerial portOne(10, 11);
void setup() {
  // Set the baud rate for the Serial port
  Serial.begin(9600);
  portOne.begin(9600);  
  pinMode(5, OUTPUT);    // sets the digital pin 13 as output
  pinMode(4,OUTPUT);
  //pinMode(12,OUTPUT);
}
int c =0;
void loop() {  
  ReciveModetransmitMode(1);
  
   // identification board;
   // board.setData("id1",50);
  //TransmitMode(1);
  int askisent = Serial.write("id01"); //portOne.write("idP");

  ReciveModetransmitMode(0);
 
  //test code  
  if(Serial.available()>0){ 
    const char incomingByte =serial.read();
    const char askirecive="ack01";
    if(strcmp(incomingByte,askirecive)==0 )
    {
      
      
      delay(1000);
      //TransmitMode(1);
      Serial.print("now setup for talk");
      portOne.write("ps");//looks for statues
      unsigned char pstatus=portOne.read()

      //int acksig =Serial.write("ackQ ");
      //portOne.write("L1");
      
    
    }
    else
      delay(5000);
  }
  ReciveModetransmitMode(0);
  const int numvaules =6;
  int sensor_states[numvaules];
  Serial.readBytes(sensor_vaules, numvaules);
  for (int i =0; i< numvaules; i++){
    if (sensor_states[i]==1){
      //heater ,alarm,water meter,rcb,heating
      
      if(i ==1){
        Serial.println("heater is on");
      }
      else{
        Serial.println("heater is off");
      }
      if(i ==2){
        Serial.println("alarm is on");
      }
      else{
        Serial.println("alarm is off");
      }
      if(i==3){
        Serial.println("water meter is on");
      }
      else{
        Serial.println("water metter is off");
      }
      if(i==4){
        Serial.println("rcb is on");
      }
      else{
        Serial.println("rcb is off");
      }
      if(i==5){
        Serial.println("heating is on"); 
      }
      else{
        Serial.println("heating is off");
      }

      else{
        Serial.println("nothing is on ");

      }
    }

  }
  ReciveModetransmitMode(0);
  int sensor_vaules[numvaules];
  Serial.readBytes(sensor_vaules , numvaules);
  for (int i = 0; i < numvaules; i++)
  {
    println(sensor_vaules[i]);
    
  }
  
    
  
}   

