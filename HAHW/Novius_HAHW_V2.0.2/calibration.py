import pyodbc
def calibration_formula():
    # Database connection details
    conn_str = (
        r"DRIVER={SQL Server};"
        r"SERVER=4MVDUGL\SQLEXPRESS;"
        r"DATABASE=NVS_HAHW_V2;"
        r"Trusted_Connection=yes;"
    )

    # Establishing connection to the database
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Query to get calibration data
    query = '''
    SELECT * FROM temperature_calibration;
    '''

    cursor.execute(query)
    rows = cursor.fetchall()
    # Initialize the list to store calibration data
    calibration_data = []

    for row in rows:
        # Extracting and converting calibration values to float
        tempMin1, tempMax1 = float(row[0].strip()), float(row[1].strip())
        cntMin1, cntMax1 = float(row[2].strip()), float(row[3].strip())
        
        tempMin2, tempMax2 = float(row[4]), float(row[5])
        cntMin2, cntMax2 = float(row[6]), float(row[7])
        
        tempMin3, tempMax3 = float(row[8]), float(row[9])
        cntMin3, cntMax3 = float(row[10]), float(row[11])
        
        tempMin4, tempMax4 = float(row[12]), float(row[13])
        cntMin4, cntMax4 = float(row[14]), float(row[15])

        # Calculating slope and offset for each sensor
        slope1 = (cntMax1 - cntMin1) / (tempMax1 - tempMin1)
        offset1 = cntMin1 - (slope1 * tempMin1)

        slope2 = (cntMax2 - cntMin2) / (tempMax2 - tempMin2)
        offset2 = cntMin2 - (slope2 * tempMin2)

        slope3 = (cntMax3 - cntMin3) / (tempMax3 - tempMin3)
        offset3 = cntMin3 - (slope3 * tempMin3)

        slope4 = (cntMax4 - cntMin4) / (tempMax4 - tempMin4)
        offset4 = cntMin4 - (slope4 * tempMin4)

        # Example PLC counts (replace these with actual values as needed)
        plc_count1 = 768
        plc_count2 = 600
        plc_count3 = 600
        plc_count4 = 600

        # Calculating actual temperatures
        t1 = (plc_count1 - offset1) / slope1
        t2 = (plc_count2 - offset2) / slope2
        t3 = (plc_count3 - offset3) / slope3
        t4 = (plc_count4 - offset4) / slope4

        # Printing the actual temperatures
        # print(f'Actual Temperature T1: {t1:.2f}°C')
        # print(f'Actual Temperature T2: {t2:.2f}°C')
        # print(f'Actual Temperature T3: {t3:.2f}°C')
        # print(f'Actual Temperature T4: {t4:.2f}°C')
        # Store calibration data in a list of tuples
    calibration_data.append((slope1, offset1, slope2, offset2, slope3, offset3, slope4, offset4))
    # Closing the database connection
    conn.close()
    # Return the list of calibration data
    return calibration_data if calibration_data else None