#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"


const char* ssid = "SUNBEAM";
const char* password = "1234567890";


const char* mqtt_server = " 172.18.4.28";   // Broker IP
const int mqtt_port = 1883;
const char* mqtt_topic = "home/temp_hum";

/* DHT Configuration */
#define DHTPIN 4
#define DHTTYPE DHT11   

WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

/* Connect to WiFi */
void setup_wifi() {
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected");
}

/* Connect to MQTT */
void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32_Publisher")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();

  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

 
  String payload = "{";
  payload += "\"temperature\":";
  payload += temperature;
  payload += ",\"humidity\":";
  payload += humidity;
  payload += "}";

  Serial.println(payload);

  client.publish(mqtt_topic, payload.c_str());

  delay(5000);  // Publish every 5 seconds
}
