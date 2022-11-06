
const int pot_pin = A0;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(5000);


  Serial.write("Hello there!"); //Writes 1 byte for each character corresponding to the ASCII char code. No line ending
  delay(1000);
  
  Serial.write(45);  //Writes 1 byte as expected
  delay(1000);

  Serial.write(128);  //Writes 1 unsigned byte. When casted to int in Java, it is interpreted as signed, so overflows to -127.
  delay(1000);
  
  Serial.write(234);  //Overflows again...
  delay(1000);

  //Lesson: for integer data transmission, create a dedicated protocol for transferring integer data.
  //Either split it into 4 bytes somehow and parse it on the receiving end or send as string/char sequence
  //Use StringBuilder for fast string appending

  
  digitalWrite(LED_BUILTIN, LOW);
}

void loop() {
  /*
  int reading = analogRead(pot_pin)/4;
  Serial.write(reading);
  Serial.println(reading);
  delay(100);
  */
}
