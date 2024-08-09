class ProxySensor:
    def __init__(self, sensor_id, ping_count, times):
        self.sensor_id = sensor_id
        self.ping_count = ping_count
        self.times = times  # List of timestamps for each ping

def get_sensor_pings():
    # Mock function to simulate sensor data retrieval
    # In a real implementation, this function would retrieve ping counts and times from a database or another source.
    # Here, we'll use hardcoded values for demonstration purposes.
    # we srored timestamp in list..ee.g[2, 4.5, 8.5, 12.5, 16.5, 20.5, 24.5, 28.5, 32.5, 36.5, 40.5, 44.5, 48.5, 52.5, 56.5])
    sensors = [
        ProxySensor('s1', 15, [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56]),
        ProxySensor('s2', 12, [2, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45]),
        ProxySensor('c1', 15, [2, 4.5, 8.5, 12.5, 16.5, 20.5, 24.5, 28.5, 32.5, 36.5, 40.5, 44.5, 48.5, 52.5, 56.5]),
        ProxySensor('c2', 12, [2.5, 5.5, 9.5, 13.5, 17.5, 21.5, 25.5, 29.5, 33.5, 37.5, 41.5, 45.5]),
        ProxySensor('e1', 14, [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55]),
        ProxySensor('e2', 16, [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64])
    ]
    return sensors

def calculate_total_axles(c_sensor, c_backup_sensor): #c is primary and c_backup is secondary sensor
    # Determine the total number of axles based on primary or backup sensor
    if c_sensor.ping_count > 0:
        return c_sensor.ping_count
    elif c_backup_sensor.ping_count > 0:
        return c_backup_sensor.ping_count
    else:
        return 0

def calculate_axle_speeds(sensor_c_times, sensor_s_times, distance):
    # Calculate speeds of axles based on time differences and distance between sensors
    speeds = []
    for c_time, s_time in zip(sensor_c_times, sensor_s_times):
        time_diff = c_time - s_time
        if time_diff > 0:  # Ensure positive time difference
            speed = distance / time_diff  # Speed = Distance / Time
            speeds.append(speed)
    return speeds

def calculate_distances_between_axles(axle_speeds, sensor_s_times):
    # Calculate distances between consecutive axles
    distances = []
    for i in range(1, len(sensor_s_times)):
        time_diff = sensor_s_times[i] - sensor_s_times[i - 1]
        if time_diff > 0:
            distance = axle_speeds[i - 1] * time_diff  # Distance = Speed * Time
            distances.append(distance)
    return distances

if __name__ == "__main__":
    DISTANCE = 10  # Distance between sensors in meters

    sensors = get_sensor_pings()
    
    # Find the primary and backup sensors for calculating axles and speeds
    c_sensor = next(sensor for sensor in sensors if sensor.sensor_id == 'c1')
    c_backup_sensor = next(sensor for sensor in sensors if sensor.sensor_id == 'c2')
    s_sensor = next(sensor for sensor in sensors if sensor.sensor_id == 's1')
    s_backup_sensor = next(sensor for sensor in sensors if sensor.sensor_id == 's2')


    # Calculate the total number of axles
    total_axles = calculate_total_axles(c_sensor, c_backup_sensor)
    print(f'Total number of axles: {total_axles}')

    # Use c1 or c2 times depending on which sensor is active
    active_c_times = c_sensor.times if c_sensor.ping_count > 0 else c_backup_sensor.times

    # Calculate axle speeds
    axle_speeds = calculate_axle_speeds(active_c_times, s_sensor.times, DISTANCE)
    for i, speed in enumerate(axle_speeds, start=1):
        print(f'Axle {i} speed: {speed:.2f} m/s')

    # Calculate distances between consecutive axles
    distances_between_axles = calculate_distances_between_axles(axle_speeds, s_sensor.times)
    unique_distances = list(set(distances_between_axles))[:4]  # Ensure only 4 unique distances

    # Print distances between axles
    for i, distance in enumerate(distances_between_axles, start=1):
        if distance in unique_distances:
            print(f'Distance between axle {i} and axle {i+1}: {distance:.2f} m')
        else:
            print(f'Distance between axle {i} and axle {i+1}: Other m')

    # Check for mismatch in the number of timestamps between active 'c' sensor and 's1' sensor
    if len(active_c_times) != len(s_sensor.times):
        print(f"Warning: The number of timestamps in 'c1' or 'c2' ({len(active_c_times)}) and 's1' ({len(s_sensor.times)}) do not match.")

    

# # Constants
# distance = 10  # Distance in meters

# # Function to calculate speed for a single axle
# def calculate_speed(s1, c1):
#     if c1 <= s1:
#         print("Error: c1 should be greater than s1")
#         return None
#     else:
#         time = c1 - s1
#         speed = distance / time
#         return speed

# # Function to process multiple axles and count the axles
# def process_axles(axle_data):
#     axle_count = 0  # Initialize axle count
#     for s1, c1 in axle_data:
#         speed = calculate_speed(s1, c1)
#         if speed is not None:
#             axle_count += 1  # Increment axle count for each valid calculation
#             print(f"Axle {axle_count} Speed: {speed} m/s")
#     return axle_count

# # Example sensor values (you will replace these with actual readings from your sensors)
# # Format: (s1, c1) for each axle
# axle_data = [
#     (1.5, 2.5),   # Axle 1: s1, c1
#     (3.0, 4.0),   # Axle 2: s1, c1
#     (5.0, 6.0),   # Axle 3: s1, c1
#     (7.0, 8.0),   # Axle 4: s1, c1
#     (9.0, 10.0)   # Axle 5: s1, c1
# ]

# # Calculate speeds for all axles and count the axles
# total_axles = process_axles(axle_data)

# # Output the total number of axles
# print(f"Total Number of Axles: {total_axles}")
