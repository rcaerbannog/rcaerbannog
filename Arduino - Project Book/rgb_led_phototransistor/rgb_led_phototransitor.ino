//Pins
const int redLEDPin = 9, greenLEDPin = 10, blueLEDPin = 11;
const int redSensorPin = A0, greenSensorPin = A1, blueSensorPin = A2;

//Variables
int redValue = 0, greenValue = 0, blueValue = 0;
int redSensorValue = 0, greenSensorValue = 0, blueSensorValue = 0;


void setup() {
  Serial.begin(9600);
  
  pinMode(redLEDPin, OUTPUT);
  pinMode(greenLEDPin, OUTPUT);
  pinMode(blueLEDPin, OUTPUT);

}

void loop() {
  redSensorValue = analogRead(redSensorPin)/4;
  delay(5);
  greenSensorValue = analogRead(greenSensorPin)/4;
  delay(5);
  blueSensorValue = analogRead(blueSensorPin)/4;
  delay(5);

  analogWrite(redLEDPin, 255-redSensorValue);
  analogWrite(greenLEDPin, 255-greenSensorValue);
  analogWrite(blueLEDPin, 255-blueSensorValue);

}
