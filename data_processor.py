import statistics
from datetime import datetime

class DataProcessor:
    def process_data(self, data):
        """
        Processes the sensor data by calculating the average, minimum, and maximum values.
        """
        timestamps, datapoints = zip(*data)
        avg_value = statistics.mean(datapoints)
        min_value = min(datapoints)
        max_value = max(datapoints)

        processed_data = {
            "timestamp": datetime.now(),
            "average_value": avg_value,
            "minimum_value": min_value,
            "maximum_value": max_value
        }

        return processed_data
