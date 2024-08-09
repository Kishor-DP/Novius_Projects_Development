--First insert values into tblTemperatureLog

INSERT INTO [dbo].[tblTemperatureLog] (
    [intTrainId], 
    [intBogiTypeId], 
    [intAxleNo], 
    [NvcharCoachNo], 
    [IntCoachPosition], 
    [decTs1], 
    [decTs2], 
    [decTs3], 
    [decTs4], 
    [decTs5], 
    [decTs6], 
    [decAxel_Speed], 
    [nvcharDescription], 
    [dtDateofCreation], 
    [dtDateofModification], 
    [ynDeleted]
) VALUES (
    1, 
    1, 
    1, 
    'A123', 
    1, 
    160.45, 
    130.56, 
    130.34, 
    130.78, 
    130.89, 
    130.12, 
    60.5, 
    'Absolute Axle Temperature', 
    GETDATE(), 
    GETDATE(), 
    0
);


--then insert into tblTrainTransaction

/****** Script for SelectTopNRows command from SSMS  ******/
INSERT INTO [HBDDB].[dbo].[tblTrainTransaction] (
    
    
    [nvcharTrainName],
    [nvcharTrainNumber],
    [nvcharDirection],
    [dtDateTime],
    [decAvg_Speed],
    [decDuration],
    [intNo_ICF],
    [intNo_LHB],
    [intNo_Wagaons],
    [intNo_Loco],
    [intNo_Bogi],
    [intOther_Stack],
    [intTotalNoOfAxles],
    [decAtmosphere_Temp],
    [nvcharDescription],
    [dtDateofCreation],
    [dtDateofModification],
    [ynDeleted]
) VALUES (
    -- Replace these values with actual data
    
    
    'Train Name',             -- nvcharTrainName
    'Train Number',           -- nvcharTrainNumber
    'Direction',              -- nvcharDirection
    '2024-05-23 15:30:00',    -- dtDateTime
    75.5,                     -- decAvg_Speed
    120,                      -- decDuration
    10,                       -- intNo_ICF
    5,                        -- intNo_LHB
    15,                       -- intNo_Wagaons
    2,                        -- intNo_Loco
    20,                       -- intNo_Bogi
    3,                        -- intOther_Stack
    64,                       -- intTotalNoOfAxles
    35.5,                     -- decAtmosphere_Temp
    'Description',            -- nvcharDescription
    '2024-05-23 14:00:00',    -- dtDateofCreation
    '2024-05-23 14:30:00',    -- dtDateofModification
    0                         -- ynDeleted
);



--program oserves which is new intTrainId is inserted into tblTrainTransaction.
saves all fetch values into differen json files process data and insertes into tblAlarms