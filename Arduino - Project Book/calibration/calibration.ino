int SENSOR_PIN = A0;
int LED_1_PIN = 4;
int sensor_max = 0;
int sensor_min = 1023;

void setup() {
  Serial.begin(9600);
  digitalWrite(LED_1_PIN, HIGH);
  delay(1000);
  digitalWrite(LED_1_PIN, LOW);
  delay(1000);


  Serial.println("Calibrating...");
  while (millis() < 5000){
    int sensorValue = analogRead(SENSOR_PIN);
    if (sensorValue < sensor_min) sensor_min = sensorValue;
    if (sensorValue > sensor_max) sensor_max = sensorValue;
    delay(100);
  }
  Serial.print("Sensor max: ");
  Serial.println(sensor_max);
  Serial.print("Sensor min: ");
  Serial.println(sensor_min);
  delay(1000);
  Serial.println("\nCalibrated sensor readings:");
  
}

void loop() {
  // put your main code here, to run repeatedly:
 /int calibratedSensorValue = map(analogRead(SENSOR_PIN), sensor_min, sensor_max, 0, 255);
  Serial.println(analogRead(calibratedSensorValue));
  delay(500);
}
