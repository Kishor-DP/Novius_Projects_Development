<?php
// sendcoach.php

$host = '103.120.176.21';
$dbname = 'noviusr1_MVISCopy';
$username = 'noviusr1_novius2';
$password = 'Yoj9IbR0y#M%';



try {
    $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    if(isset($_GET['CoachId'])) {
        $code = $_GET['CoachId'];
        $query = "SELECT * FROM [noviusr1_MVISCopy].[noviusr1_noviusr1].[MVIS_left] AS c
        WHERE EXISTS (
            SELECT 1
            FROM [noviusr1_MVISCopy].[dbo].[Coachn] AS m
            WHERE m.CoachId = c.CoachId
        ) AND c.CoachId = :CoachId";
$stmt = $conn->prepare($query);
$stmt->bindParam(':CoachId', $code);
$stmt->execute();
$data = $stmt->fetchAll(PDO::FETCH_ASSOC);
        
        // Output JSON data
        echo json_encode($data);
        
    } else {
        echo "No code specified.";
    }

} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
