const int piezo_pin = 8;
const int pt_pin = A0;
int pt_vale;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(piezo_pin, OUTPUT);
  tone(piezo_pin, 500);
  delay(1000);
  noTone(piezo_pin);
  pinMode(LED_BUILTIN, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  int pt_value = analogRead(pt_pin);
  int frequency = map(pt_value, 0, 1023, 50, 4000);
  Serial.print("Phototransistor value: ");
  Serial.print(pt_value);
  Serial.print(", Frequency: ");
  Serial.println(frequency);
  tone(piezo_pin, frequency);
  delay(20);
}
