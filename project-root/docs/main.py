#include <DHT.h>

#define DHTPIN 2     // Pino conectado ao sensor DHT11
#define DHTTYPE DHT11   // Tipo de sensor DHT
#define FANPIN 3    // Pino conectado ao ventilador

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  pinMode(FANPIN, OUTPUT);
  dht.begin();
}

void loop() {
  float temperature = dht.readTemperature();

  if (isnan(temperature)) {
    Serial.println("Falha ao ler do sensor DHT11");
    return;
  }

  if (temperature > 25.0) { // Temperatura limite de 25°C
    digitalWrite(FANPIN, HIGH); // Liga o ventilador
  } else {
    digitalWrite(FANPIN, LOW); // Desliga o ventilador
  }

  delay(2000); // Espera 2 segundos antes de ler novamente
}