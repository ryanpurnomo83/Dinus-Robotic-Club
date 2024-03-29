 #include <Servo.h> //Arduino Servo Library 

Servo ESC;  // ESC için bir obje tanımlanıyor. 

float value;    // Analog pin A1 den veri okuma için değişken tanımlaması. 
void setup()
{
  Serial.begin(9600);
  ESC.attach(26);  // Pin 3 den PWM sinyal çıkışı.
}

void loop() { 
  
//   for(int i = 0; i < 50; i++)
//     {
//      value=value+analogRead(27); // Potansiyometreden gelen değeri daha kararlı veriye çevirmek için 50 kez toplanıp ortalamasının alınması.
//      delay(1);
//     }  
     
  value=analogRead(27); // Ortalama değer
  value=map(value, 0, 4095, 0, 180); // Analog girişten okunan değerin ESC nin anlayacağı değerlere çevrilmesi. 
  ESC.write(value);                    // Potansiyometreden gelen değere göre ESC / servo konumunu ayarlar. 
  Serial.print("Değer= ");
  Serial.println(value);
  }
