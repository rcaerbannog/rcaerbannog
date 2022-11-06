const int sensor_pin = A0;
const int gate_pin = 9;

void setup() {
  pinMode(gate_pin, OUTPUT);

}

void loop() {
  int motorState = map(analogRead(sensor_pin), 0, 1023, 255, 0);
  analogWrite(gate_pin, motorState);

}
