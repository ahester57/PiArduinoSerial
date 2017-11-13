// Austin Hester
// 11/11/17
// Arduino Serial USB Communication
char rcvChar;
boolean newData = false;

void setup() {
  Serial.begin(9600);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(2, INPUT);
}

void loop() {
  recvInfo();
  lightLED();
}

void recvInfo() {
  if (Serial.available() > 0) {
    rcvChar = Serial.read();
    newData = true;
  }
}

void lightLED() {
  int led = (rcvChar - '0');
  while (newData) {
    digitalWrite(led, HIGH);
    delay(200);
    digitalWrite(led, LOW);
    newData = false;
  }
}
