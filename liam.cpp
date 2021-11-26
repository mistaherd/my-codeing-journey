#include "mbed.h"
#include "Servo.h"
#include <iostream>
#include "MMA7660.h"
#include "Ping.h"

using namespace std;

Serial pc(USBTX, USBRX); // tx, rx

Ticker flipper;

DigitalIn joy_up(p15);
DigitalIn joy_down(p12);

Servo myservo1(p21);
Servo myservo2(p22);
Ping Pinger(p24);

AnalogIn p1(p19);
AnalogIn p2(p20);

MMA7660 MMA(p28, p27);

float servo_position ;
            
int main (){
 
     string A ;
     cout << "command list :, \n \r"; 
     cout << "1 (rotate servo 180 degrees), \n \r";
     cout << "2(rotate servo 90 degrees), \n \r";
     cout << "3 (rotate servo 0 degrees), \n \r";
     cout << "4 (user type in degress), \n \r";
     cout << "5 (servo controled by accelerometer ), \n \r";
     cout << "6 (controled by joystick), \n \r";
     cout << "7 (servo controled by pot), \n \r";
     cout << "8 (tilt up and down), \n \r";
     cout << "9 (control tilt with joystick) \n \r";
     cout << "10 (sound sytem controls servo) \n \r";
    while(1){
         
              cin >> A ;
              
               if(A =="1")
               {
                   myservo1 = 1 ;
                   myservo2 = 1 ;
               }
            
            else if(A== "2")
            {
                   myservo1 =  0.5 ;
                   myservo2 = 0.5 ;
            }
           
            else if(A=="3")
            {
                myservo1 = 0;
                myservo2 = 0;
            }
          
             else if(A =="4")
            {
                float x ;
                cout << "please enter in the degree you want the servo to be at go (limit is 180 degrees  be sure to hit enter after  command \n\r" ;
                cin >> x;    // waits for the user to type something and hit enter to finsh
                wait(0.01);
                myservo1 = x/180;
                myservo2 = x/180 ;
            }
            
            else if(A== "5")
            {
                       float x=0 ,y=0;
                       x = (x + MMA.x() );
                       y = (y -(MMA.y() ));
                       myservo1 = x;
                       myservo2 =y ;
                        //pc.printf("mma.x is = %f ,mma.y is = %f \n \r",MMA.x() ,MMA.y()); use this to see vaules the servo uses   
            }
           
         else if (A == "6")
            {
                if (joy_up)
                {
                   //rotates when joy is up. move by 10%
                    myservo1= myservo1+ 0.1;
                    myservo2 = myservo2 + 0.1;
                     wait(0.1);    
                }
                else if(joy_down)
                {
                    myservo1= myservo1- 0.1;
                    myservo2 = myservo2 - 0.1;
                     wait(0.1);    
                }
            }
           
          else if(A == "7")
            {
                 //makes pot control servo
                 myservo1=p1;
                 myservo2=p2; 
                 float z ;
                 z= p1 ;
                 cout << " %f is what is the pot reading \n \r ",z;
                
            }
            
            else if(A == "8")
            {
                //tilt up / down
                myservo1 = 0;
                myservo2 = 1;
                wait(3);   
                myservo1 = 1;
                myservo2 = 0;
            }
            
             else if(A =="9")
            {
                 if (joy_up)
                {
                    myservo1= myservo1+ 0.1;
                    myservo2 = myservo2 - 0.1;
                     wait(0.1);    
                }
                else if(joy_down)
                {
                    myservo1= myservo1- 0.1;
                    myservo2 = myservo2 + 0.1;
                     wait(0.1);    
                }
            }
           
            else if (A =="10")
            {    
            while(1)
            {
               Pinger.Send();    
               wait_ms(30);
               myservo1= (Pinger.Read_cm())/604 ;// 605 becasue it never gonna be 0 
               myservo2 =(Pinger.Read_cm())/604 ;
               
            }
                
                // exit while loop code her 
            }
            else if(A =="11")
            {
                string C;
                cout << "options ; 'S0' = soft start ,'S0' = soft stop /n/r" ;
                cin  >> C;
                
                if(C== "s0")
                {
                    
                }
            }
            
            
            }
            }
//// funtions


    
    
    
