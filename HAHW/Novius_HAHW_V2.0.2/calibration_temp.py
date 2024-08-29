import pyodbc
from datetime import datetime

class TemperatureSensorSystem:
    def __init__(self, voltage_readings, conn_str):
        self.voltage_readings = voltage_readings
        self.conn_str = conn_str
        self.temperatures = {}

    class TemperatureSensor:
        def __init__(self, voltage):
            self.voltage = voltage

        def convert_to_celsius(self):
            # Assuming a linear relationship where 5V corresponds to 100°C
            temperature_celsius = (self.voltage / 5.0) * 100.0
            return temperature_celsius

    def convert_voltages_to_temperatures(self):
        for sensor, voltage in self.voltage_readings.items():
            if voltage is None:
                self.temperatures[sensor] = None
            else:
                sensor_obj = self.TemperatureSensor(voltage)
                self.temperatures[sensor] = sensor_obj.convert_to_celsius()

    def insert_temperature_data(self):
        # Database connection parameters
        with pyodbc.connect(self.conn_str) as conn:
            cursor = conn.cursor()
            # Insert data into the database
            cursor.execute("""
                INSERT INTO tblTemperatureLog (
                    intTrainId,
                    intBogiTypeId,
                    intAxleNo,
                    NvcharCoachNo,
                    IntCoachPosition,
                    decTs1,
                    decTs2,
                    decTs3,
                    decTs4,
                    decTs5,
                    decTs6,
                    decAxel_Speed,
                    nvcharDescription,
                    dtDateofCreation,
                    dtDateofModification,
                    ynDeleted
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                1,  # Default value for intTrainId
                1,  # Default value for intBogiTypeId
                1,  # Default value for intAxleNo
                'A1',  # Default value for NvcharCoachNo
                1,  # Default value for IntCoachPosition
                self.temperatures.get("t1", None),
                self.temperatures.get("t2", None),
                self.temperatures.get("t3", None),
                self.temperatures.get("t4", None),
                self.temperatures.get("t5", None),
                self.temperatures.get("t6", None),
                0.0,  # Default value for decAxel_Speed
                'Default Description',  # Default value for nvcharDescription
                datetime.now(),  # Default value for dtDateofCreation
                datetime.now(),  # Default value for dtDateofModification
                0  # Default value for ynDeleted
            ))
            # Commit the transaction
            conn.commit()

    def run(self):
        self.convert_voltages_to_temperatures()
        self.insert_temperature_data()
        self.print_results()

    def print_results(self):
        # Print the results
        for sensor, temperature in self.temperatures.items():
            print(f"Sensor {sensor}: {'Null' if temperature is None else f'{temperature:.2f}°C'}")


if __name__ == "__main__":
    # Example voltage readings for sensors t1 to t6
    voltage_readings = {
        "t1": 1.0,  # replace with actual voltage readings
        "t2": 2.0,
        "t3": 0.0,
        "t4": 7.8,
        "t5": 4.5,
        "t6": 5.0
    }

    # Database connection string
    conn_str = (
        "DRIVER={SQL Server};"
        "SERVER=4MVDUGL\KISHOR;"
        "DATABASE=HBDDB;"
        "Trusted_Connection=yes;"
    )

    # Create and run the temperature sensor system
    system = TemperatureSensorSystem(voltage_readings, conn_str)
    system.run()
