const int pot_pin = A0;

void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.write(analogRead(pot_pin)/4);
  delay(200);
}
