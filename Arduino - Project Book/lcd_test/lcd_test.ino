#include <LiquidCrystal.h>
LiquidCrystal lcd(12,11,5,4,3,2);
int a = 65;

//Note: lcd has 40 positions per line. Position (40, 0) overflows to position (0, 0).
//When printing, putting characters at (40, 0) will overflow to (0, 1)

//scrolling will put characters at (0, 1) onto (39, 0) and (0, 0) to (39, 1)
//printing while scrolling may have unintended side effects. It seems that if c character is printed when another character is being moved into the same spot, the printed character is shifted to the other line

byte smiley[8] = {
  B00000,
  B10001,
  B00000,
  B00000,
  B10001,
  B01110,
  B00000,
  B11011
};

void setup() {
  lcd.begin(16, 2);
  lcd.print("0123456789abcdefghij0123456789ABCDEFGHIJZ");
  
  //lcd.autoscroll();
  Serial.begin(9600);

  for (int i = 0; i < 40; i++){
    lcd.scrollDisplayLeft();
    delay(200);
  }
  delay(1000);
}

void loop(){
  /*
  if (Serial.available()){
    lcd.write(Serial.read());
    lcd.scrollDisplayLeft();
  }
  */
  
  
  
  
}
