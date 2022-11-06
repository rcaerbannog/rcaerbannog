const int sensorPin = A0;
const float baselineTemp = 26.0;


void setup() {
  Serial.begin(9600);
  for (int pinNumber = 2; pinNumber < 5; pinNumber++){
    pinMode(pinNumber, OUTPUT);
    digitalWrite(pinNumber, LOW);
  }

}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorVal = analogRead(sensorPin);
  Serial.print("Sensor value: ");
  Serial.print(sensorVal);
  float voltage = (sensorVal/1024.0)*5.0;
  Serial.print("; Volts: ");
  Serial.print(voltage);
  float temperature = (voltage-0.5)*100;
  Serial.print("; Temperature (°C): ");
  Serial.println(temperature);

  if (temperature < baselineTemp+2){
    digitalWrite(4, LOW);
    digitalWrite(3, LOW);
    digitalWrite(2, LOW);
  }
  else if (temperature < baselineTemp+3){
    digitalWrite(4, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(2, LOW);
  }
  else if (temperature < baselineTemp+4){
    digitalWrite(4, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(2, LOW);
  }
  else{
    digitalWrite(4, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(2, HIGH);
  }
  delay(500);
}
