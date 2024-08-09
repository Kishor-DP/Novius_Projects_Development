# Input string
input_str = 'C1,    10,  31   5  16  11  197343000,   716,     0,'

# Strip extra spaces and split the string by commas
parts = [part.strip() for part in input_str.split(',') if part.strip()]

# Print parts for debugging
print(f"Parts: {parts}")

# Check the length of parts to avoid IndexError
if len(parts) != 5:
    print("Error: Unexpected number of elements in the input string.")
else:
    # Extract values
    c1 = parts[0]
    count = int(parts[1])
    time_stamp = parts[2]
    t1 = int(parts[3])
    t2 = int(parts[4])

    # Print the extracted values
    print(f"c1 = {c1}")
    print(f"count = {count}")
    print(f"time_stamp = {time_stamp}")
    print(f"t1 = {t1}")
    print(f"t2 = {t2}")
