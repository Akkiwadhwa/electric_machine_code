#include <Wire.h>
#include <OneWire.h>
#include <Adafruit_MLX90614.h>
#include "Nextion.h"
#include <DFRobot_MLX90614.h>
#include <DFRobot_OxygenSensor.h>
#include <DFRobot_AirQualitySensor.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

//variable definition
double temp_amb;
double temp_obj;
int ledPin = 13;
String command;

void setup()
{
  Serial.begin(9600);
  mlx.begin();         //Initialize MLX90614
  //Serial.println("Temperature Sensor MLX90614");
  pinMode(ledPin, OUTPUT);
  delay(1000);
}
 
void loop()
{//code snippet for Temperature sensor
  temp_amb = mlx.readAmbientTempC();
  //temp_obj = mlx.readObjectTempC();

  //Serial Monitor output
  //Serial.print("Room Temp = ");
  Serial.println(temp_amb);
  //Serial.print("Object temp = ");
  //Serial.println(temp_obj);
  delay(500);

//code snippet for LED BLINKER
   if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(ledPin, HIGH);
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);
    } else if (command == '2') {
      for (int i = 0; i < 10; i++) {
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
        delay(500);
      }
    }
  }
}
