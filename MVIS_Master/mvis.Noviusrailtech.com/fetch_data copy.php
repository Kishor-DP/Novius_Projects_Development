<?php
// fetch_data.php

$host = '103.120.176.21';
$dbname = 'noviusr1_MVISCopy';
$username = 'noviusr1_novius2';
$password = 'Yoj9IbR0y#M%';


try {
    $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    if(isset($_GET['timestamp'])) {
        $timestamp = $_GET['timestamp'];
        $query = "SELECT Sr_No, Code, Component, Parameter, Status FROM MVIS_left WHERE Time_Stamp = :timestamp";
        $stmt = $conn->prepare($query);
        $stmt->bindParam(':timestamp', $timestamp);
        $stmt->execute();
        $data = $stmt->fetchAll(PDO::FETCH_ASSOC);
        echo json_encode($data);
    } elseif(isset($_GET['code'])) {
        $code = $_GET['code'];
        $query = "SELECT *
FROM [noviusr1_MVISCopy].[dbo].[MVIS_left] AS c
WHERE EXISTS (
    SELECT 1
    FROM [noviusr1_MVISCopy].[dbo].[Gridviewtbl] AS m
    WHERE m.Code = c.Code
)
AND c.Code = :code
ORDER BY CONVERT(datetime, c.Time_Stamp_Gridviewtbl, 107) DESC";
        $stmt = $conn->prepare($query);
        $stmt->bindParam(':code', $code);
        $stmt->execute();
        $data = $stmt->fetchAll(PDO::FETCH_ASSOC);
        
        // Output separate grid for each row
        foreach ($data as $row) {
            echo "<div class='grid'>";
            foreach ($row as $key => $value) {
                echo "<div><strong>$key:</strong> $value</div>";
            }
            echo "</div>";
        }
    } else {
        $query = $query = "SELECT TOP (292) *
        FROM [noviusr1_MVISCopy].[dbo].[Gridviewtbl];";
        $stmt = $conn->query($query);
        $data = $stmt->fetchAll(PDO::FETCH_ASSOC);
        echo json_encode($data);
    }

} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
