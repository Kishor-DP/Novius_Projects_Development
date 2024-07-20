<!DOCTYPE html>
<html>
<head>
    <title>Display Image in Grid</title>
    <style>
        .grid-it {
            width: 100px; /* Set the width of your grid div */
            height: 100px; /* Set the height of your grid div */
            background-size: cover; /* Ensure the background image covers the entire div */
            background-position: center; /* Center the background image */
        }
    </style>
</head>
<div class="grid-it"></div>
<body>
    <table>
    <?php
        $host = '103.120.176.21';
        $dbname = 'noviusr1_MVIS';
        $username = 'noviusr1_noviusr1';
        $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM ICF_Detected");
            
            // Execute the query
            $stmt->execute();
            
            // Fetch all rows as associative array
            $rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
            
             // Reverse the order of the rows array
             $rows = array_reverse($rows);
        
            // Check if any rows were returned
            if (!$rows) {
                echo "No rows found.";
            }
        } catch (PDOException $e) {
            echo "Connection failed: " . $e->getMessage();
        }
        ?>
        <thead>
            <tr>
                <th style="width: 10px;">Time_Stamp</th>
                <th style="width: 10px;">Primary_Suspension</th>
                <!-- Add other column headers as needed -->
            </tr>
        </thead>
        <tbody>
            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                    <tr>
                        <td><?php echo $row['Time_Stamp']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_encode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Primary_Suspension']; ?></a></td>
                        <!-- Add other columns as needed -->
                    </tr>
                <?php endforeach; ?>
            <?php endif; ?>
        </tbody>
    </table>

    

    <script>
        function showImage(imageUrl) {
            document.querySelector('.grid-it').style.backgroundImage = 'url("' + imageUrl + '")';
        }
    </script>
</body>
</html>
