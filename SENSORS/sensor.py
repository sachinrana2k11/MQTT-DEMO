import random

class sensor:
    def __init__(self):
        self.sensor1 = "temperature"
        self.sensor2 = "humidity"

    def get_data(self):
        data = {
            "temperature":str(random.randint(10,30)),
            "humdity":str(random.randint(40,60)),
        }
        return data

# obj = sensor()
# print(obj.get_data())