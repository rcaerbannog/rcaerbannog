void setup(){
  Serial.begin(9600);
}

void loop(){
  int sensorVal = analogRead(A5);
  Serial.println(sensorVal);
  delay(500);
}
