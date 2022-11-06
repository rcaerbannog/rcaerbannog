const int control_pin = 9;

//Practical switching time limit for octocoupler is around 15ms. Maybe can drop to 12.
void setup() {
  pinMode(control_pin, OUTPUT);

}

void loop() {
  digitalWrite(control_pin, HIGH);
  delay(12);
  digitalWrite(control_pin, LOW);
  delay(12);
  //25 hz
  

}
