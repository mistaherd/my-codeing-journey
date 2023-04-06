#include <SoftwareSerial.h>
#include<string.h>



void ReciveMode(int state){
    if(state = 1){
    digitalWrite(5,LOW);
    }
    else{
    digitalWrite(4,HIGH);
    }

}


void TransmitMode(int state){
    if(state =1){
    digitalWrite(5,HIGH);
    }
    else{
    digitalWrite(5,LOW);
    }
}
int setup=0
//software serial
// Set up a new SoftwareSerial object with RX in digital pin 10 and TX in digital pin 11
SoftwareSerial portOne(10,11);
void setup() {
  // Set the baud rate for the Serial port
  Serial.begin(9600);
  portOne.begin(9600);  
  pinMode(5, OUTPUT);    // sets the digital pin 13 as output
  pinMode(4,OUTPUT);
  //pinMode(12,OUTPUT);
}

void loop() {  
  ReciveMode(1);
  delay(10); 
  TransmitMode(0);
 
  if(portOne.avaialbe()>0){
    int incomingByte =portOne.read();
    int asciirecive="id01";
    int c=0;
    if(incomingByte==asciirecive){
      TransmitMode(1);
      ReciveMode(0);
      delay(500);
      portone.write("ack01");
  
    }
  }
  else {
    setup=0;
  }
  
 if(setup==1){

  TransmitMode(0);
  ReciveMode(1);
  if(portOne.avaialble()>0){
    int commandin =portOne.read();
    int lutcomm= "ps";
    if(strcmp(incomingByte,askirecive)==0 )
        
  }
 }
 
 
}  

