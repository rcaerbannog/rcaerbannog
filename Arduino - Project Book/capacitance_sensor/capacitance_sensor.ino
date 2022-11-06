#include <CapacitiveSensor.h>
CapacitiveSensor capSensor = CapacitiveSensor(4,2);
int threshold = 1000;
const int led_pin = 12;

void setup() {
  Serial.begin(9600);
  pinMode(led_pin, OUTPUT);

}

void loop() {
  long sensorValue = capSensor.capacitiveSensor(30);
  Serial.println(sensorValue);
  if (sensorValue > threshold) digitalWrite(led_pin, HIGH);
  else digitalWrite(led_pin, LOW);
  delay(100);
}
