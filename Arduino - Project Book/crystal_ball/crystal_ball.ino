#include <LiquidCrystal.h>
LiquidCrystal lcd(12,11,5,4,3,2);

const int switch_pin = 6;
int switchState = 0;
int prevSwitchState = HIGH;
int reply;

char *replies[8] = {"Yes", "Ask again", "Most likely", "Certainly", "Unsure", "Outlook good", "Doubtful", "No"};



void setup() {
  lcd.begin(16, 2);
  pinMode(switch_pin, INPUT);
  lcd.print("Ask the");
  lcd.setCursor(0, 1);
  lcd.print("Crystal Ball!");
}

void loop() {
  switchState = digitalRead(switch_pin);
  if (switchState != prevSwitchState){
    if (switchState == HIGH){
      reply = random(8);
      lcd.clear();
      lcd.print("The reply is:");
      lcd.setCursor(0, 1);
      lcd.print(replies[reply]);
      delay(1000);
    }
    prevSwitchState = switchState;
  }
  delay(10);
}
