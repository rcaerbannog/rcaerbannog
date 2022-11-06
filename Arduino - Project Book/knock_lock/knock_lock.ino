#include <Servo.h>
Servo myServo;

const int piezo_pin = A0;
const int switch_pin = 2;
const int led_red_pin = 13;
const int led_yellow_pin = 12;
const int led_green_pin = 11;

const int NOISE_THRESHOLD = 10;
const int QUIET_KNOCK = 20;
const int LOUD_KNOCK = 200;
boolean locked = false;
int numberOfKnocks = 0;

unsigned long attemptStartTime = 0;

void setup() {
  // put your setup code here, to run once:
  myServo.attach(9);
  pinMode(switch_pin, INPUT);
  pinMode(led_red_pin, OUTPUT);
  pinMode(led_yellow_pin, OUTPUT);
  pinMode(led_green_pin, OUTPUT);
  Serial.begin(9600);

  digitalWrite(led_red_pin, HIGH);
  digitalWrite(led_yellow_pin, HIGH);
  digitalWrite(led_green_pin, HIGH);
  delay(1000);
  myServo.write(0);
  digitalWrite(led_red_pin, LOW);
  digitalWrite(led_yellow_pin, LOW);
  digitalWrite(led_green_pin, HIGH);
  Serial.println("The box is unlocked!");
  delay(1000);
}

void loop() {
  //If box is unlocked, check to see if the lock button is pressed. If so, lock the box.
  if (!locked){
    int switchVal = digitalRead(switch_pin);
    if (switchVal == HIGH){
      locked = true;
      numberOfKnocks = 0;
      digitalWrite(led_green_pin, LOW);
      digitalWrite(led_red_pin, HIGH);
      myServo.write(90);
      Serial.println("The box is locked!");
      delay(1000);
    }
  }

  //If box is locked, execute knock checking logic
  else {
    int knockVal = analogRead(piezo_pin);
    if (knockVal > QUIET_KNOCK && knockVal < LOUD_KNOCK){
      numberOfKnocks++;
      digitalWrite(led_yellow_pin, HIGH);
      Serial.print(3-numberOfKnocks);
      Serial.println(" knocks to go!");
      delay(500);
      digitalWrite(led_yellow_pin, LOW);
      Serial.print("Valid knock of value: ");
      Serial.println(knockVal);
    }
    else if (knockVal > NOISE_THRESHOLD){
      Serial.print("INVALID KNOCK OF VALUE: ");
      Serial.println(knockVal);
      delay(100);
    }
    
    if (numberOfKnocks >= 3){
      locked = false;
      myServo.write(0);
      delay(50);
      digitalWrite(led_green_pin, HIGH);
      digitalWrite(led_red_pin, LOW);
      Serial.println("The box is unlocked!");
      delay(1000);
    }
  }
  delay(10);
}
