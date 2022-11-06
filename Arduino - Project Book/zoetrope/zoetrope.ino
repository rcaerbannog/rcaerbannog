const int on_off_pin = 5;
const int direction_switch_pin = 4;
const int pot_pin = A0;
const int enable12_pin = 9;
const int input1_pin = 3;
const int input2_pin = 2;

int prevOnOffState = LOW;
int prevDirectionSwitchState = LOW;

bool isOn = false;
bool isCW = false;

void setup() {
  pinMode(on_off_pin, INPUT);
  pinMode(direction_switch_pin, INPUT);
  pinMode(enable12_pin, OUTPUT);
  pinMode(input1_pin, OUTPUT);
  pinMode(input2_pin, OUTPUT);
}

void loop() {
  int onOffState = digitalRead(on_off_pin);
  int directionSwitchState = digitalRead(direction_switch_pin);
  int motorSpeed = analogRead(pot_pin)/4;

  if (onOffState != prevOnOffState){
    if (onOffState == HIGH) isOn = !isOn;
    prevOnOffState = onOffState;
  }
  if (directionSwitchState != prevDirectionSwitchState){
    if (directionSwitchState == HIGH) isCW = !isCW;
    prevDirectionSwitchState = directionSwitchState;
  }
  
  if (isOn)analogWrite(enable12_pin, motorSpeed);
  else analogWrite(enable12_pin, 0);
  
  if (isCW){
      digitalWrite(input1_pin, HIGH);
      digitalWrite(input2_pin, LOW);
  }
  else {
      digitalWrite(input1_pin, LOW);
      digitalWrite(input2_pin, HIGH);
  }

  delay(10);
}
