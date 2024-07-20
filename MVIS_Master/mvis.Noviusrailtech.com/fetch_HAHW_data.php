<?php
// fetch_alarm_data.php


$host = '103.120.176.21';
$dbname = 'noviusr1_MVISCopy';
$username = 'noviusr1_novius2';
$password = 'Yoj9IbR0y#M%';



try {
    $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    if(isset($_GET['code'])) {
        $code = $_GET['code'];
        $query = "SELECT intAxleNo, IntCoachPosition, decTs1, decTs2, decTs3, 1decTs4 Status FROM tblTemperatureLog WHERE dtDateofCreation = :timestamp";
        $stmt = $conn->prepare($query);
        $stmt->bindParam(':code', $code);
        $stmt->execute();
        $data = $stmt->fetchAll(PDO::FETCH_ASSOC);
        
        echo json_encode($data);
    } else {
        echo "No code specified.";
    }

} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
