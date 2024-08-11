from calibration import calibration_formula

# Assigning PLC counts
plc_count1 = 768
plc_count2 = 600
plc_count3 = 600
plc_count4 = 600

# Fetch calibration data
calibration_data = calibration_formula()

# Iterate over calibration data and calculate actual temperatures
for slopes_offsets in calibration_data:
    slope1, offset1, slope2, offset2, slope3, offset3, slope4, offset4 = slopes_offsets

    # Calculating actual temperatures
    t1 = (plc_count1 - offset1) / slope1
    t2 = (plc_count2 - offset2) / slope2
    t3 = (plc_count3 - offset3) / slope3
    t4 = (plc_count4 - offset4) / slope4

    # Printing the actual temperatures
    print(f'Actual Temperature T1: {t1:.2f}°C')
    print(f'Actual Temperature T2: {t2:.2f}°C')
    print(f'Actual Temperature T3: {t3:.2f}°C')
    print(f'Actual Temperature T4: {t4:.2f}°C')
