import random
from datetime import datetime

# explain the code in comments
from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from device import Device
from dashboard import Dashboard

def main():
    sensor = Sensor(0, 100)
    #print (sensor)
    
    data_processor = DataProcessor()
   
    communication = Communication("https://central-server.example.com")
    device = Device(sensor, data_processor, communication)
    
    dashboard = Dashboard()

    device.collect_data(10)
    processed_data = device.process_data()
    #print ('Dolfi', processed_data)
    device.send_data_to_server(processed_data)
    device.receive_data_from_server()

    dashboard.display_data(device.data)
    dashboard.display_analytics(processed_data)

if __name__ == "__main__": # why this line is needed? (is a conditional statement that checks if the current script is being run as the main program. If it is, the code inside the if statement will be executed. This is used to ensure that certain code only runs when the script is run directly, and not when it is imported as a module into another script.)
    
    main()
