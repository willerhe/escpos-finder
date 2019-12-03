import paho.mqtt.client as mqtt
import json


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("prod/printer/10009")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    order = json.loads(str(msg.payload, 'utf-8'))
    details = order['details'][0]
    print(order['total'])
    print(order['tableId'])
    print(details['skus'])


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("101.132.43.15", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
