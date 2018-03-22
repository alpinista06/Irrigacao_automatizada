#include <Servo.h>
#define Leitura A0

Servo servo1; // cria um objeto servo1
int Umidade;
int Nivel;


void setup()
{
  Serial.begin(9600);
  pinMode(Leitura, INPUT);
  servo1.attach(5); // anexa o servomotor (físico), no pino 5, ao objeto servo1 (lógico)
}

void loop()
{
  servo1.write(5); // Escreve o ângulo para o servomotor
  //Le o valor do pino A0 do sensor
  Umidade = analogRead(Leitura);
  Nivel = (100-(Umidade/10.24));

  if (Umidade < 300)
  {
    Serial.println(Nivel);
  }else
  if (Umidade < 800)
  {
    Serial.println(Nivel);
    servo1.write(127);
  }else
  if (Umidade < 1024)
  {
    Serial.println(Nivel);
    servo1.write(255);
  }
  delay(1000);
}
