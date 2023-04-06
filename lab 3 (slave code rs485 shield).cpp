#include <SoftwareSerial.h>
#include<string.h>
#include <bitset>
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

void setup()
{
 Serial.begin(9600);
 pinMode(led,OUTPUT);
 pinMode(EN,OUTPUT);
}
void loop()
{
  ReciveModetransmitMode(0);//Enable low, RS485 shield waiting to receive data
  if(Serial.available()>0){
    const char incomingByte= Serial.read();
    const char asciirecive= "id01";
    if(strcmp(incomingByte, asciirecive)==0){
      ReciveModetransmitMode(1);
      delay(100);
      Serial.write("ack01");
     
    }
  }
  int setup=Serial.read();
  if(setup==1){
    ReciveModetransmitMode(0);
    if(Serial.avaiable()>0){
        const char commandin =Serial.read();
        const char lutcomm="ps";
        if(strcmp(commandin,lutcomm)==0){
          // first binaray is to check whats on
          //heater ,alarm,water meter,rcb,heating
          ReciveModetransmitMode(1);
          bitset<6> b("10101");
          Serial.write(b);
          delay(1000);
          Serial.write("end");
          delay(100);
          //next reading vaule of the sensor
          
        }
      
        
    }
    ReciveModetransmitMode(0);
    if(Serial.avaiable()>0){
    const char end_of_array =Serial.read();
    const char end ="end";
    if(strcmp(end,end_of_array)==0);{
    const int numvaules =6;
    int sensor_vaules[numvaules] ={25,0,100,0,255};
    ReciveModetransmitMode(1);     
    Serial.write(sensor_vaules ,numvaules);
    delay(1000);
    Serial.write("end")
    ReciveModetransmitMode(0);
    const char endcom ="ENDCOM";
    end_of_array = Serial.read();
    if(strcmp(endcom,end_of_array)==0){
      break;
    }    
    }
    
  
    }
  }

}
