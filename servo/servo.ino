#include <Servo.h>

Servo myservo1;
int angle = 0;
String msg = "";
byte parseStart = 0;

void setup() {
  myservo1.attach(10);
  Serial.begin(9600);

}

void loop() {
  myservo1.write(angle);
  if (Serial.available())
  {
    char in = Serial.read();
    if(!(in == '\n' || in == '|r'))
    {
      if(in == ';')
      {
        parseStart = 1;
      }
      if(in == '#')
      {
        parseStart = 2;
      }
      if ((parseStart == 2) && (in != '#'))
      {
        msg += in;
      }
    }
  }

  if(parseStart == 1)
  {
    int message = msg.toInt();
    if (message == 0)
    {
      myservo1.write(45);
      delay(3000);
      angle = 45;
    }
    if (message == 1)
    {
      myservo1.write(135);
      delay(3000);
      angle = 135;
      
    }
    if (message == 2)
    {
      myservo1.write(180);
      delay(3000);
      angle = 180;
      
    }
  }
   
}
