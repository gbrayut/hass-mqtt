#!/usr/bin/env python3
"""This is a simple mqtt python script"""
import os
import sys
import ssl
import time
import paho.mqtt.client as mqtt

# Variables and callbacks
mqttserver = os.getenv('MQTT_SERVERNAME', 'mqtt') #Use env var MQTT_SERVERNAME or default mqtt
mqttusername = os.getenv('MQTT_USERNAME', None) #Use env variables to set username/password
mqttpassword = os.getenv('MQTT_PASSWORD', None)
clientid = "simple-{HOSTNAME}-{PID}".format(HOSTNAME=os.uname()[1], PID=os.getpid())
def exit(status=0):
    """Used to disconnect and exit with given status code"""
    print("Disconnecting and exiting with status",status)
    mqttclient.disconnect()
    sys.exit(status)
def on_log(client, userdata, level, buf):
    """Used by mqtt client to generate log messages"""
    print("log: ", buf)
def on_connect(client, userdata, flags, rc):
    """Used by mqtt client after connecting."""
    print("Connected to %s:%s flags=%s rc=%s" % (client._host, client._port, flags, rc))
    if rc != 0:
        print("Connection error: rc", rc, mqtt.error_string(rc))
        exit(10+rc)
def on_message(client, userdata, msg):
    """Callback when mqtt client receives a message"""
    time.sleep(1)
    #print("received message =", str(msg.payload.decode("utf-8")))
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))


# Example of using https://pypi.org/project/paho-mqtt/ client

print("Starting {}".format(clientid))
mqttclient = mqtt.Client(client_id=clientid)
#mqttclient.enable_logger(logger=None)
if mqttusername != None:
    mqttclient.username_pw_set(mqttusername, mqttpassword)
mqttclient.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
mqttclient.tls_insecure_set(False) #Set to true to bypass certificate validation
mqttclient.on_log = on_log
mqttclient.on_connect = on_connect
mqttclient.on_message = on_message
mqttclient.on_publish = on_publish
mqttclient.on_subscribe = on_subscribe
#mqttclient.will_set(topic=,payload=)
mqttclient.connect(mqttserver, 4883, 60)
#mqttclient.connect_srv("example.com", 60)
#mqttclient.subscribe("$SYS/broker/version", 0)


#mqttclient.loop_start()
mqttclient.publish("topic/test", "Hello from "+clientid)

rc = 0
while rc == 0:
    rc = mqttclient.loop()

print("rc: "+str(rc))

print("Finished")

exit(0)
