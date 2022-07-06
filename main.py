import datetime
import json, time
from CLOUD.mqgen import Generic_Mqtt
from SENSORS.sensor import sensor

with open("CONFIG/config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print("Config Read successfully For MQTT")

mqtt_obj = Generic_Mqtt()
sensor_obj = sensor()

while 1:
    sensor_in_data = sensor_obj.get_data()
    final_data = {
        "DevcieId": data["DEVICE_INFO"]["DEVICEID"],
        "OrgId": data["DEVICE_INFO"]["ORG_ID"],
        "AppId": data["DEVICE_INFO"]["APP_ID"],
        "Payload": sensor_in_data,
        "TimeStamp": str(datetime.datetime.now())
    }
    print(final_data)
    mqtt_obj.MQTT_Send_Data(json.dumps(final_data))
    time.sleep(data["DEVICE_INFO"]["TIME_SENT"])
