import random
from datetime import datetime

class Dashboard:
    def display_data(self, data):
        """
        Displays the sensor data in a formatted manner.
        """
        print("Timestamp\tData")
        print("===================")
        for timestamp, datapoint in data:
            print(f"{timestamp}\t{datapoint}")

    def display_analytics(self, analytics):
        """
        Displays the analytics results (max, min, and average values).
        """
        max_value = max(analytics)
        min_value = min(analytics)
        avg_value = sum(analytics) / len(analytics)

        print(f"Maximum value: {max_value}")
        print(f"Minimum value: {min_value}")
        print(f"Average value: {avg_value}")

