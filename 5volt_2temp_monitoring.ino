
//for reading voltage
int analogInput[5] = {A0, A1, A2, A3, A4};

float vout[5] = {0.0, 0.0, 0.0, 0.0, 0.0};
float vin[5] = {0.0, 0.0, 0.0, 0.0, 0.0};

float R1 = 30000.0; //  
float R2 = 7500.0; // 

//for reading temperature
// Affectation of pins
#define CS0 10
#define CS1 9
#define MISO 12
#define SCLK 13

// Call of libraries
#include <SPI.h>
#include "Adafruit_MAX31855.h"

Adafruit_MAX31855 Temp0(SCLK, CS0, MISO); // Creation of the object0
Adafruit_MAX31855 Temp1(SCLK, CS1, MISO); // Creation of the object1

void setup(){
   pinMode(analogInput[0], INPUT);
   pinMode(analogInput[1], INPUT);
   pinMode(analogInput[2], INPUT);
   pinMode(analogInput[3], INPUT);
   pinMode(analogInput[4], INPUT);
   Serial.begin(115200);
}
void loop(){
  vout[0] = (analogRead(analogInput[0]) * 5.0) / 1024.0;
  vin[0] = vout[0] / (R2/(R1+R2));
  Serial.print(vin[0],2);
  Serial.print(",");
  
  vout[1] = (analogRead(analogInput[1]) * 5.0) / 1024.0;
  vin[1] = vout[1] / (R2/(R1+R2));
  Serial.print(vin[1],2);
  Serial.print(",");
  
  vout[2] = (analogRead(analogInput[2]) * 5.0) / 1024.0;
  vin[2] = vout[2] / (R2/(R1+R2));  
  Serial.print(vin[2],2);
  Serial.print(",");
  
  vout[3] = (analogRead(analogInput[3]) * 5.0) / 1024.0;
  vin[3] = vout[3] / (R2/(R1+R2));  
  Serial.print(vin[3],2);
  Serial.print(",");
  
  vout[4] = (analogRead(analogInput[4]) * 5.0) / 1024.0;
  vin[4] = vout[4] / (R2/(R1+R2));  
  Serial.print(vin[4],2);
  Serial.print(",");
  
  
  Serial.print(Temp0.readCelsius()); // Acquisition of temp0
  Serial.print(",");
  
  Serial.println(Temp1.readCelsius()); // Acquisition of temp1
  
  
  delay(500);
}
