const int on_off_pin = 13;
const int enable12_pin = 10;
const int enable34_pin = 9;
const int input1_pin = 3;
const int input2_pin = 2;
const int input3_pin = 4;
const int input4_pin = 5;

int prev_on_off_state = LOW;
boolean isOn = false;

void setup() {
  // put your setup code here, to run once:
  pinMode(on_off_pin, INPUT);
  pinMode(enable12_pin, OUTPUT);
  pinMode(enable34_pin, OUTPUT);
  pinMode(input1_pin, OUTPUT);
  pinMode(input2_pin, OUTPUT);
  pinMode(input3_pin, OUTPUT);
  pinMode(input4_pin, OUTPUT);

  //analogWrite(enable12_pin, 150);
  digitalWrite(input1_pin, HIGH);
  digitalWrite(input2_pin, LOW);
  //analogWrite(enable34_pin, 150);
  digitalWrite(input3_pin, HIGH);
  digitalWrite(input4_pin, LOW);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  int on_off_state = digitalRead(on_off_pin);
  if (on_off_state != prev_on_off_state && on_off_state == HIGH){
    isOn = !isOn;
    if (isOn){
      analogWrite(enable12_pin, 255);
      analogWrite(enable34_pin, 255);
    }
    else{
      analogWrite(enable12_pin, 0);
      analogWrite(enable34_pin, 0);
    }
  }
  prev_on_off_state = on_off_state;
}
