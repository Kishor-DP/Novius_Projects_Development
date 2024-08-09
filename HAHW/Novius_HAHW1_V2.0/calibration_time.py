class ProxySensors:
    def __init__(self, hours):
        self.hours = hours
    
    def convert_to_minutes(self):
        """
        Convert hours to minutes.
        """
        return self.hours * 60

def main():
    # Example hour readings for sensors s1 to s6
    hour_readings = {
        "s1": 1.5,  # replace with actual hour readings
        "s2": 2.3,
        "c1": 0.5,
        "c2": 1.0,
        "e1": 0.0, 
        "e2": 0.5
    }

    # Convert hour readings to minutes
    minutes_data = {}
    for sensor, hours in hour_readings.items():
        if hours is None:
            minutes_data[sensor] = None
        else:
            sensor_obj = ProxySensors(hours)
            minutes_data[sensor] = sensor_obj.convert_to_minutes()

    # Print the results
    for sensor, minutes in minutes_data.items():
        print(f"Sensor {sensor}: {'Null' if minutes is None else f'{minutes:.2f} minutes'}")

if __name__ == "__main__":
    main()
