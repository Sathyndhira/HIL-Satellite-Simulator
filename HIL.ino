const int LED_pin = 13;

void setup() {
  Serial.begin(9600);
  pinMode(LED_pin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    int battery = Serial.parseInt();

    if (battery < 50) {
      digitalWrite(LED_pin, HIGH);
      Serial.println(1.5);
    } else {
      digitalWrite(LED_pin, LOW);
      Serial.println(5.0);
    }
  }
}
