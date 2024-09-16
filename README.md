# extensao-iot-python
  Controle de Ventilador com Sensor de Temperatura
Este projeto utiliza um sensor de temperatura DHT11 e um Arduino para controlar um ventilador com base na temperatura lida. O objetivo é manter um ambiente confortável, acionando o ventilador quando a temperatura ultrapassar um limite pré-determinado.

  Descrição do Projeto
O projeto consiste em um sistema que monitora a temperatura ambiente e aciona um ventilador quando a temperatura ultrapassa um valor específico. O sistema utiliza um sensor DHT11 para ler a temperatura e um Arduino para processar os dados e controlar o ventilador.

  Componentes Utilizados
Arduino Uno: Microcontrolador para ler os dados do sensor e controlar o ventilador.
Sensor DHT11: Sensor de temperatura e umidade.
Ventilador: Dispositivo que será controlado pelo Arduino.
Transistor NPN (como o 2N2222): Para controlar o ventilador.
Resistor de 10kΩ: Para o sensor DHT11.
Cabos de Conexão: Para ligar os componentes.
Diagrama do Circuito
O diagrama do circuito está disponível em /docs/circuit_diagram.png.


  Código-Fonte
O código-fonte está localizado em /src/main.ino. Este arquivo contém o código necessário para ler os dados do sensor DHT11 e controlar o ventilador.

  Exemplo de Código
cpp
Copiar código
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
  Configuração do Projeto
    Montagem do Circuito:

Conecte o pino VCC do DHT11 ao pino 5V do Arduino.
Conecte o pino GND do DHT11 ao GND do Arduino.
Conecte o pino DATA do DHT11 ao pino digital 2 do Arduino.
Conecte o pino de controle do ventilador ao pino digital 3 do Arduino, utilizando um transistor NPN para controlar o ventilador.
Carregar o Código:

Abra o Arduino IDE.
Carregue o código presente em /src/main.ino no seu Arduino.
Documentação
A documentação adicional está disponível na pasta /docs, incluindo o diagrama do circuito.
