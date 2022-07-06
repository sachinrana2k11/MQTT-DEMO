import sys
import json
import paho.mqtt.client as mqtt
from termcolor import colored


class Generic_Mqtt():
    def __init__(self):
        with open("CONFIG/config.json", "r") as jsonfile:
            self.data = json.load(jsonfile)
            print("Config Read successfully For MQTT")
        self.MQTT_client = mqtt.Client()
        self.MQTT_Connect()

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.data["CLOUD"]["TOPIC_SUB"])
        print("Connected and subscribe already")

    def on_message(self, client, userdata, msg):
        in_data = json.loads(msg.payload.decode("utf-8"))
        print(in_data)

    def MQTT_Connect(self):
        try:
            # temp = self.data["USR"]
            # print(temp)
            self.MQTT_client.username_pw_set(self.data["CLOUD"]["MQTT_USR"], self.data["CLOUD"]["MQTT_PWD"])
            self.MQTT_client.on_connect = self.on_connect
            self.MQTT_client.on_message = self.on_message
            self.MQTT_client.connect(self.data["CLOUD"]["MQTT_BROKER"], self.data["CLOUD"]["MQTT_PORT"])
            self.MQTT_client.loop_start()
            print(colored("SUCCESSFULLY CONNECTED TO MQTT BROKER", "green"))
        except:
            e = sys.exc_info()[0]
            print(colored("FAILED TO CONNECT MQTT SERVER CHECK CONNECTION - " + str(e), "red"))
            pass

    def MQTT_Send_Data(self, payload):
        try:
            self.MQTT_client.publish(topic=self.data["CLOUD"]["TOPIC_PUB"], payload=payload,
                                     qos=self.data["CLOUD"]["QOS"])
            print(colored("PUBLISHING  DATA TO MQTT-:" + str(payload), "green"))
            return True
        except:
            e = sys.exc_info()[0]
            print(colored("EXCEPTION IN SENDING DATA BY GENERIC MQTT - " + str(e), "red"))
            pass
