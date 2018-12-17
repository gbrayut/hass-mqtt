# hass-mqtt

Home Assistant MQTT projects and notes

# Setup MQTT broker in Home Assistant

There is a [built in broker](https://www.home-assistant.io/docs/mqtt/broker/), but I decided to use the [addon broker in hassos](https://github.com/hassio-addons/addon-mqtt/blob/v0.2.2/README.md) instead. There was an [issue using TLS](https://github.com/hassio-addons/addon-mqtt/issues/15) between the containers, but otherwise the setup was pretty straight forward. More details:

- Docs: 
https://www.home-assistant.io/docs/mqtt
- Enable discovery for setting up sensors https://www.home-assistant.io/docs/mqtt/discovery/
- JSON examples: https://www.home-assistant.io/docs/mqtt/processing_json/

# First MQTT sensor

Home Assistant can generate sensors dynamically if you enable the [MQTT discovery option](https://www.home-assistant.io/docs/mqtt/discovery/). Once enabled the following topic/payloads will create new entities.

```
Topic: homeassistant/binary_sensor/garden/config
Payload: {"name": "garden", "device_class": "motion"}

Topic: homeassistant/binary_sensor/garden/state
Payload: ON
Payload: OFF

To remove the sensor send an empty payload to the same config topic
```

- More testing options: https://www.home-assistant.io/docs/mqtt/testing/

# More resources

- MQTT Test client: http://workswithweb.com/mqttbox.html