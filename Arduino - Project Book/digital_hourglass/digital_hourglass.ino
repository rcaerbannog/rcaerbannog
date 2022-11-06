const int switchPin = 8;
unsigned long previousTime = 0;
unsigned long previousBlinkTime = 0;
int switchState = 0;  //HIGH is upright, LOW is down
int previousSwitchState = 0;

int led = 2;   //Next LED to turn on. From 2 to 7 inclusive
long interval = 2000;
long blinkInterval = 500;
bool blinkHigh = false;

void setup() {
  for (int x = 2; x < 8; x++) pinMode(x, OUTPUT);
  pinMode(switchPin, INPUT);

}

void loop() {
  unsigned long currentTime = millis();
  if ((led < 1 || led > 8) && currentTime - previousBlinkTime > blinkInterval){
    previousBlinkTime += blinkInterval;
    int blinkState = (blinkHigh)? HIGH : LOW;
    for (int x = 2; x < 8; x++) digitalWrite(x, blinkState);
    blinkHigh = !blinkHigh;
    return;
  }
  if (currentTime - previousTime > interval){
    previousTime = currentTime;
    digitalWrite(led, HIGH);
    if (previousSwitchState == 1) led++;
    else led--;
    return;
  }
  switchState = digitalRead(switchPin);
  if (switchState != previousSwitchState){
    for (int x = 2; x < 8; x++) digitalWrite(x, LOW);
    led = (switchState == 1)? 2 : 7;
    previousTime = currentTime;
    previousSwitchState = switchState;
  }
}
