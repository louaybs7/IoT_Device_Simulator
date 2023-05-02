import random
from datetime import datetime
class Sensor:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def read_data(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "timestamp": current_time,
            "value": random.uniform(self.min_value, self.max_value)
        }
