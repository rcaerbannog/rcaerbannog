const int keys[15] = {1001,1007,969,988,931,960,854,896,696,775,509,640,412,552,338};
const int frequencies[25] = {196,208,220,233,247,262,277,294,311,330,349,370,392,415,440,466,494,523,554,587,622,659,698,740,784};

int musicKeys[2][13];
int offset; //Offset relative to G3
int remove1;
int remove2;
int previousNote = -1;
const int tolerance = 4;  //inclusive

const int sensor_pin = A5;
const int piezo_pin = 2;
const int octave_pin = 13;
const int shift_key_pin = 12;
int prev_shift_key_pin_state = LOW;

void setup() {
  Serial.begin(9600);
  createKeyboard(5);
  pinMode(piezo_pin, OUTPUT);
}

void loop() {
  int sensorVal = analogRead(sensor_pin);
  int shift_key_pin_state = digitalRead(shift_key_pin);
  if (shift_key_pin_state != prev_shift_key_pin_state){
    if (shift_key_pin_state == HIGH){
      //Check the next white key offset. If offset is 12 already (largest value), revert to offset 0
      if (offset == 12) createKeyboard(0);
      else if (offset == 4 || offset == 9) createKeyboard(offset+1); //If current offset is B or E, the next black key is missing so go up 1
      else createKeyboard(offset+2);
    }
    prev_shift_key_pin_state = shift_key_pin_state;
    Serial.println(shift_key_pin_state);
  }
  for (int i = 0; i < 13; i++){
    if (abs(sensorVal-musicKeys[0][i]) <= tolerance){
      if (digitalRead(octave_pin) == HIGH) tone(piezo_pin, 2*musicKeys[1][i], 50);  //n notes up is 2^(n/12). 1 octave is 12 notes up.
      else tone(piezo_pin, musicKeys[1][i], 50);
      previousNote = i;
      delay(10);
      break;
    }
  }
  previousNote = -1;
  delay(10);
}

void createKeyboard(int newOffset){
  offset = newOffset;
  int offsetMod = offset % 12;
  //Offset 0: index 5 and 10
  //Remove the two non-existent black keys for the key corresponding to this offset by setting them to an impossible value (-100)
  switch (offsetMod){
    case 0:
      remove1 = 5;
      remove2 = 11;
      break;
    case 2:
      remove1 = 3;
      remove2 = 9;
      break;
    case 4:
      remove1 = 1;
      remove2 = 7;
      break;
    case 5:
      remove1 = 5;
      remove2 = 13;
      break;
    case 7:
      remove1 = 3;
      remove2 = 11;
      break;
    case 9:
      remove1 = 1;
      remove2 = 9;
      break;
    case 10:
      remove1 = 7;
      remove2 = 13;
      break;
    default:
      Serial.println("Error: can't create keyboard starting on black key. Defaulted to middle C (offset 5). ");
      createKeyboard(5);  //Middle C
      return;
  }
  remove2 -= 1;
  int a = 0;
  for (int i = 0; i < 13; i++){
    if (i == remove1 || i == remove2) a++;
    musicKeys[0][i] = keys[a];
    musicKeys[1][i] = frequencies[offset+i];
    a++;
  }
  Serial.print("Offset: ");
  Serial.println(offset);
  Serial.println("MusicKeys: ");
  for (int i = 0; i < 13; i++){
    Serial.print(musicKeys[0][i]);
    Serial.print(", ");
    Serial.println(musicKeys[1][i]);
  }
  Serial.println("Everything alright?\n");
}
