<!DOCTYPE html>
<html lang="en">
    <title>Novius RailTech MVIS</title>
<head>
    <link rel="shortcut icon" type="x-icon" href="images/top-icon - Copy.jpeg">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
    
  @import url('https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;500&family=Secular+One&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Rubik&display=swap');
  @import url('https://cdn-uicons.flaticon.com/2.1.0/uicons-regular-rounded/css/uicons-regular-rounded.css');
  body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #e9e9e9!important;
        }
        ::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-thumb {
    background-color: rgb(0, 242, 255);
    border-radius: 20px;
}
        header {
            
            color: white;
            padding: 0px;
            text-align: center;
        }

        nav {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 3px;
            background:linear-gradient(to top, rgb(3, 3, 3), rgb(108, 109, 109));
        }

        .flex-container {
            display: flex;
        }

      
       
    
        button {
            font-size: 13px;
            color: #fff;
            height: 35px;
            width: 135px;
            background: linear-gradient(to top, rgb(3, 3, 3), rgb(108, 109, 109));
            border: 0px;
        }
        button:hover {
        background:linear-gradient(to top, rgb(212, 3, 3), rgb(248, 166, 166));
        color:white;
        } 
      
   
      
       

       
        .f1tab{
        height: 420px;
        overflow-y: auto;
        }
        .flex-2 {
            width: 1000px;
            /* overflow-x: auto;
            overflow-y: auto; */
            padding: 0px 10px;
            height: 560px;
           
        }

        table {
           
            border-collapse: collapse;
      
        }
        th, td {
            width: 20px;
        }

       td {
            border: 1px solid #ddd;
            padding: 2px;
            text-align: center;
            font-size: small;
            fon
            t-family: 'Rubik', sans-serif;
        }

        table #tb0{
            width:400px ;
        }
       #tb0 th{
            background-color: #375392;
    color: white;
    padding: 5px;
    border: 1px solid #ddd;
    font-size: small;
    font-family: 'Rubik', sans-serif;
width: 70px;
}

.t1{
    overflow-y: auto;
}
.t2{
    overflow-y: auto;
}

#tb1 th{
    background-color: #ed2160;
  
    color: white;
    padding: 5px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: small;
    font-weight: bold;
    width: 70px;
}
#tb1 td{
    
    border: 1px solid #ddd;
  
    padding: 5px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: small;
    
}
#tb2 th{
    background-color: #f2750f;
    width: 70px;
    color: white;
    padding: 5px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: small;
    font-weight: bold;
}
#tb2 td{
   
    border: 1px solid #ddd;
  
    padding: 5px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: small;
    
}


#tb6 th{
    background-color: #0f2df2;
    width: 70px;
    color: white;
    padding: 5px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: small;
    font-weight: bold;
}
#tb6 td{
   
    border: 1px solid #ddd;
  
    padding: 5px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: small;
    
}



        .flex-3 {
            width: 300px;
            overflow-y: auto;
            padding: 0px;
            background-color: #fff;
            height: 560px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .grid-container {
            display: grid;
        }

        .grid-item {
           /* border: 1px solid #ccc;*/
            padding: 5px;
            height: 35px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            /* overflow-y: auto; */
            display: flex;
            width: 998px
    /* overflow-x: scroll; */
        }
        .grid-it {
           /* border: 1px solid #ccc;*/
            padding: 10px;
            height: 67px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);    
            display: flex;
            justify-content: flex-start;
            gap: 20px;
            background-repeat: no-repeat;
            background-position: center;
            background-size: contain;
        }

        .flex-table {
            display: flex;
        }

        .flex-table div {
            flex: 1;
           
            
            margin: 5px;
        }
        .Tdetail{
            
           
            background-color: rgb(0, 0, 0); color: white; 
            padding: 6px; 
            text-align:center;
            border-top-left-radius: inherit;
            border-top-right-radius: inherit;
         
            font-family: 'Rubik', sans-serif;
    font-size: x-small;
    text-transform: uppercase;
    font-weight: bold;
        }
     
        .save {
    justify-content: center;
    display: flex;
    align-items: center;
}
.savess {
    justify-content: center;
    display: grid;
    align-items: center;
}
#tb3 tbody tr:nth-child(odd) {
    background-color:#dce6f2; /* Adjust as needed */
    }

   #tb3 tbody tr:nth-child(even) {
      background-color: #ffffff; /* Adjust as needed */
    }
    .vi{
        display: inline-block;
    color: #ffffff;
    cursor: pointer;
    font-family: 'Rubik', sans-serif;
    font-size: x-small;
    text-transform: uppercase;
    font-weight: bold;
        }
.bc{
    background-color: black;
    color: #fff;
}
#abc{

    width: 90px;
    font-size: x-small;
    border-radius: inherit;
}
#textboxes4 {
            width: 100%;
            height: 20px;
            position: relative;
            overflow: hidden;
}
.grid-itt{
    display: grid;
    height: 473px;
    background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            overflow-y: auto;
}
.date{
           
           display: grid;
           padding: 2px;
           border-radius: 2px;
           text-align: justify;
           gap: 4px;
           font-size: small;
           font-weight: bold;
       }

.info{
    display: grid;
    grid-template-columns: 70% 5% 25%;
    background: #dce6f2;
    padding: 8px 0px;
}
.info2{
    display: grid;
    grid-template-columns: 70% 5% 25%;
    background: white;
    padding: 8px 0px;
}
.l1{
        color: black;
       }
       .l3{
        color: rgb(0, 0, 0);
        text-align: center;
       }
  
   
    

        .textbox-container2 {
            position: absolute;
    top: 40%;
    left: 55%;
    transform: translate(-50%, -50%);
    width: 700px;
        }
    
     
  



/* ----------------------------------------------- */


       .datesub{
        background: #dce6f2;
           display: grid;
           padding: 2px;
           border-radius: 2px;
           text-align: justify;
           gap: 4px;
           font-size: x-small;
           font-weight: bold;
           grid-template-columns: repeat(2 , 45%);
       }

       .button-box{
    display: grid;
    justify-content: space-around;
    grid-template-columns: repeat(2 ,45%);
    padding: inherit;
}
.grid-itfst {
           /* border: 1px solid #ccc;*/
            padding: 10px;
            height: 135px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);    
            display: flex;
            justify-content: space-between;
            gap: 20px;

        }
        .left-column121, .right-column121 {
      width: 45%;
    }

    .image-box121 {
      height: 45px;
      width: 100%;
      margin-bottom: 5px;
      background-size: cover;
      background-position: center;
    }
        .fst-grid {
    height: 40px;
    background-color: #fff;
    /* border-radius: 8px; */
    /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); */
    /* overflow-y: auto; */
    display: grid;
    background: linear-gradient(45deg, #000000, transparent);
}
.subbb1{
    display: flex;
    justify-content: space-evenly;
}
.subbb2{
   
    font-family: 'Rubik', sans-serif;
    font-size: small;
    text-transform: uppercase;
    font-weight: bold;
    color: white;

}
.subbb3{
   
   color: white;
   font-family: 'Rubik', sans-serif;
   font-size: medium;
   text-transform: uppercase;


}
.dateee{
           
           display: grid;
           padding: 2px;
           border-radius: 2px;
           text-align: justify;
   
           font-size: small;
           font-weight: bold;
         
       }
#tb3 tr:nth-child(even) {
    
      background-color: blue;
     
}
#tb3 th:nth-child(even) {

    background-color: blue;
    color: white;
}

/* -------------------------------------------------------- */
.scroll-button {
      position:relative;
      
      background-color: #3498db;
      color: #fff;
      border: none;
      padding: 10px;
      cursor: pointer;
    }

    /* .scroll-button.left {
      left: 0;
    }

    .scroll-button.right {
      right: 0;
    } */
    .scroll-container {
      position: relative;
      width: 900px; /* Adjust the width as needed */
      overflow: hidden;
    }

    .scroll-content {
      display: flex;
      transition: transform 0.5s ease;
    }

    </style>
</head>
<body>


    <div style="height: 10px;"></div>

    <div class="flex-container">
     

        <div class="flex-2">
            <div class="grid-container">
            <div class="fst-grid">
            <div class="subbb1">
                        <div class="subbb3">Mvis Simple View</div>
                        <div class="subbb3"> <input type="number" id="coachInput" placeholder="Coach Position" oninput="addCoaches()"> </div>
                    </div>
<div class="subbb1">
    <div class="subbb2">Left Hand Side View</div>
    <div class="subbb2">Right Hand Side View</div>
</div>
                    
</div>
                <!-- Add 7x20 grid items here -->
                <div class="grid-item" id="gridContainer">
                <button class="scroll-button left">&larr; Left</button>
  <div class="scroll-container">
    <div class="scroll-content">
      <!-- Your content goes here -->
      <button class="savess">
        <div id="textboxes4"></div>
        <div class="bc">Coach-6</div>
      </button>
      <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-1</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-2</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-3</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-4</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-5</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-6</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-7</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-8</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-9</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-1</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-2</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-3</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-4</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-5</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-6</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
        <div class="bc">Coach-7</div>
    </button>
    <button  class="savess">
        <div id="textboxes4">

        </div>
      <!-- Repeat the pattern for more items -->
    </div>
  </div>
  <button class="scroll-button right">Right &rarr;</button>

  
                </div>
<div class="grid-itt">
<div class="grid-itfst">
        <div class="left-column121">
            <div class="image-box121" style="background-image: url('path_to_image1.jpg');"></div>
            <div class="image-box121" style="background-image: url('path_to_image2.jpg');"></div>
            <div class="image-box121" style="background-image: url('path_to_image3.jpg');"></div>
            <div class="image-box121" style="background-image: url('path_to_image4.jpg');"></div>
          </div>
          <div class="right-column121">
            <div class="image-box121" style="background-image: url('path_to_image5.jpg');"></div>
            <div class="image-box121" style="background-image: url('path_to_image6.jpg');"></div>
            <div class="image-box121" style="background-image: url('path_to_image7.jpg');"></div>
            <div class="image-box121" style="background-image: url('path_to_image8.jpg');"></div>
          </div>
        </div>
        
        <div class="grid-it">
                                        <div class="t2">
                                        
                                            <table id="tb6">
                                            <?php
       $host = '103.120.176.21';
       $dbname = 'noviusr1_pune_mum_end';
       $username = 'noviusr1_novius2';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM Hot_Axle_left");
            
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
                                    <th>Axle_No</th>
                                    <th>Coach_Position</th>
                                    <th>MP_side_Axle_Temp</th>
                                    <th>Ap_side_Axle_Temp</th>
                                    <th>Wheel_Temp</th>
                                   
                                </tr>
                            
                            </thead>
                            <tbody>

                            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['Axle_No']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Coach_Position']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected2.jpg')); ?>')"><?php echo $row['MP_side_Axle_Temp']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected3.jpg')); ?>')"><?php echo $row['Ap_side_Axle_Temp']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['Wheel_Temp']; ?></a></td>



                    </tr>
                <?php endforeach; ?>
            <?php endif; ?>

                                <!-- Rows -->
                             
                    </tbody>
                                        </table>
                                        <script>
        function showImage(imageUrl) {
            document.querySelector('.grid-it').style.backgroundImage = 'url("' + imageUrl + '")';
        }
    </script>
                                        </div>
                                        
                                                        </div>

                <div class="grid-it">
<div class="t1">
<style>
    #tb5{
            width: 100%;
            
        }
        #tb5 th {
        display: none;
    }
        td {
            padding: 8px; /* Adjust padding as needed */
        }
        .auto-width {
            flex: 1;
        }
    </style>
    
    <table id="tb0">
    <?php
       $host = '103.120.176.21';
       $dbname = 'noviusr1_pune_mum_end';
       $username = 'noviusr1_noviusr1';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM MVIS_left");
            // ORDER BY Sr_No DESC OFFSET 0 ROWS FETCH NEXT 200 ROWS ONLY
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
                                    <th>Sr_No</th>
                                    <th>Code</th>
                                    <th>Component</th>
                                    <th>Parameter</th>
                                    <th>Status</th>
                                   
                                </tr>
                            
                            </thead>
                            <tbody>

                            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['Sr_No']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Code']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected2.jpg')); ?>')"><?php echo $row['Component']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected3.jpg')); ?>')"><?php echo $row['Parameter']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['Status']; ?></a></td>



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
</div>
<div class="t2">

    <table id="tb0">
    <?php
       $host = '103.120.176.21';
       $dbname = 'noviusr1_pune_mum_end';
       $username = 'noviusr1_noviusr1';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM MVIS_right");
            
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
                                    <th>Sr_No</th>
                                    <th>Code</th>
                                    <th>Component</th>
                                    <th>Parameter</th>
                                    <th>Status</th>
                                   
                                </tr>
                            
                            </thead>
                            <tbody>

                            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['Sr_No']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Code']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected2.jpg')); ?>')"><?php echo $row['Component']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected3.jpg')); ?>')"><?php echo $row['Parameter']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['Status']; ?></a></td>



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
</div>
                </div>
                <div class="grid-it">
                    <div class="t1">
                        <table id="tb1">
                        <?php
       $host = '103.120.176.21';
       $dbname = 'noviusr1_pune_mum_end';
       $username = 'noviusr1_noviusr1';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM Alarm_left");
            
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
                                    <th>Sr_No</th>
                                    <th>Code</th>
                                    <th>Components</th>
                                    <th>Parameter</th>
                                    <th>Alarm</th>
                                   
                                </tr>
                            
                            </thead>
                            <tbody>

                            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['Sr_No']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Code']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected2.jpg')); ?>')"><?php echo $row['Components']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected3.jpg')); ?>')"><?php echo $row['Parameter']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['Alarm']; ?></a></td>



                    </tr>
                <?php endforeach; ?>
            <?php endif; ?>

                                <!-- Rows -->
                             
                    </tbody>
                    </table>
                    <script>
        function showImage(imageUrl) {
            document.querySelector('.grid-it').style.backgroundImage = 'url("' + imageUrl + '")';
        }
    </script>
                    </div>
                    <div class="t1">
                        <table id="tb1">
                        <?php
       $host = '103.120.176.21';
       $dbname = 'noviusr1_pune_mum_end';
       $username = 'noviusr1_noviusr1';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM Alarm_right");
            
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
                                    <th>Sr_No</th>
                                    <th>Code</th>
                                    <th>Components</th>
                                    <th>Parameter</th>
                                    <th>Alarm</th>
                                   
                                </tr>
                            
                            </thead>
                            <tbody>

                            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['Sr_No']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Code']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected2.jpg')); ?>')"><?php echo $row['Components']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected3.jpg')); ?>')"><?php echo $row['Parameter']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['Alarm']; ?></a></td>



                    </tr>
                <?php endforeach; ?>
            <?php endif; ?>

                                <!-- Rows -->
                             
                    </tbody>
                    </table>
                    <script>
        function showImage(imageUrl) {
            document.querySelector('.grid-it').style.backgroundImage = 'url("' + imageUrl + '")';
        }
    </script>
                    </div>
                                    </div>
                                    <div class="grid-it">
                                        <div class="t2">
                                        
                                            <table id="tb2">
                                            <?php
       $host = '103.120.176.21';
       $dbname = 'noviusr1_pune_mum_end';
       $username = 'noviusr1_noviusr1';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM Warning_left");
            
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
                                    <th>Sr_No</th>
                                    <th>Code</th>
                                    <th>Components</th>
                                    <th>Parameter</th>
                                    <th>Warning</th>
                                   
                                </tr>
                            
                            </thead>
                            <tbody>

                            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['Sr_No']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Code']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected2.jpg')); ?>')"><?php echo $row['Components']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected3.jpg')); ?>')"><?php echo $row['Parameter']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['Warning']; ?></a></td>



                    </tr>
                <?php endforeach; ?>
            <?php endif; ?>

                                <!-- Rows -->
                             
                    </tbody>
                                        </table>
                                        <script>
        function showImage(imageUrl) {
            document.querySelector('.grid-it').style.backgroundImage = 'url("' + imageUrl + '")';
        }
    </script>
                                        </div>
                                        <div class="t2">
                                        
                                            <table id="tb2">
                                            <?php
       $host = '103.120.176.21';
       $dbname = 'noviusr1_pune_mum_end';
       $username = 'noviusr1_noviusr1';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM Warning_right");
            
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
                                    <th>Sr_No</th>
                                    <th>Code</th>
                                    <th>Components</th>
                                    <th>Parameter</th>
                                    <th>Warning</th>
                                   
                                </tr>
                            
                            </thead>
                            <tbody>

                            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['Sr_No']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Code']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected2.jpg')); ?>')"><?php echo $row['Components']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected3.jpg')); ?>')"><?php echo $row['Parameter']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['Warning']; ?></a></td>



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
                                        </div>
                                                        </div>


            </div>
        </div>
            
        </div>
   
        <div class="flex-3">
        <div class="Tdetail">Train Details :
            2023-12-14 9:30</div>
            <!-- Add 12 rows with 2 flex divs in each row here -->

            <div class="dateee">
            <table id="tb3">

            <?php
       $host = '103.120.176.21';
       $dbname = 'noviusr1_pune_mum_end';
       $username = 'noviusr1_noviusr1';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM Train_Details ORDER BY Direction DESC OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY");
            
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

  <tr>
  
    <th>Direction</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
    <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Direction']; ?></a></td>
    <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Avg_Speed(Kmph)</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Avg_Speed(Kmph)']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Total_No_Of_Locos</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Total_No_Of_Locos']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Total_No_Of_Axles</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Total_No_Of_Axles']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>No_Of_Coaches/Wagons</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                    <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['No_Of_Coaches/Wagons'];?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Total_No_Of_Alarms</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Total_No_Of_Alarms']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Total_No_Of_Warning</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Total_No_Of_Warning']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Bogie_View_Components</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Bogie_View_Components']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>
        </tr>
  <tr>
    <th>Side_View_Components</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Side_View_Components']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>
        </tr>
  <tr>
    <th>Bottom_Components</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Bottom_Components']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Top_View_Components</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Top_View_Components']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>MaxTemp_MP</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MaxTemp_MP']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>MinTemp_MP</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MinTemp_MP']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>MaxTemp_AP</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
    <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MaxTemp_AP']; ?></a></td>
  
    <?php endforeach; ?>
            <?php endif; ?>
        </tr>
  <tr>
    <th>MinTemp_AP</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
    <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MinTemp_AP']; ?></a></td>
  
    <?php endforeach; ?>
            <?php endif; ?>
        </tr>
          
             
</tbody>
</table>
<script>
        function showImage(imageUrl) {
            document.querySelector('.grid-it').style.backgroundImage = 'url("' + imageUrl + '")';
        }
        createButtons();
    </script>


            </div>
                
            </div>
            <!-- Repeat for 11 more rows -->
        </div>
    </div>
    

     </div>
     <script>
    function addCoaches() {
        // Get the number of coaches from the input
        var numberOfCoaches = parseInt(document.getElementById("coachInput").value);

        // Validate the input
        if (isNaN(numberOfCoaches) || numberOfCoaches <= 0) {
            alert("Please enter a valid number greater than 0.");
            return;
        }

        // Clear the existing buttons
        document.getElementById("gridContainer").innerHTML = "";

        // Create buttons based on the input
        for (var i = 1; i <= numberOfCoaches; i++) {
            // Create a new button element
            var newButton = document.createElement("button");
            newButton.id = "abc";
            newButton.className = "savess";

            // Create div for textboxes4
            var textboxesDiv = document.createElement("div");
            textboxesDiv.id = "textboxes4";

            // Create div for coach name
            var coachNameDiv = document.createElement("div");
            coachNameDiv.className = "bc";
            coachNameDiv.innerHTML = "Coach-" + i;

            // Append textboxes4 and coach name divs to the button
            newButton.appendChild(textboxesDiv);
            newButton.appendChild(coachNameDiv);

            // Add the new button to the grid item container
            var gridContainer = document.getElementById("gridContainer");
            gridContainer.appendChild(newButton);
        }
    }
 
    $(document).ready(function () {
      let currentIndex = 0;

      function scrollContent(direction) {
        const scrollContent = $('.scroll-content');
        const items = $('.savess');
        const itemWidth = items.eq(0).outerWidth() + 10; // Include margin

        if (direction === 'right') {
          currentIndex += 3;
          if (currentIndex > items.length - 3) {
            currentIndex = 0;
          }
        } else if (direction === 'left') {
          currentIndex -= 3;
          if (currentIndex < 0) {
            currentIndex = items.length - 3;
          }
        }

        const translateValue = -currentIndex * itemWidth;
        scrollContent.css('transform', `translateX(${translateValue}px)`);
      }

      $('.scroll-button.right').on('click', function () {
        scrollContent('right');
      });

      $('.scroll-button.left').on('click', function () {
        scrollContent('left');
      });
    });


</script>

</body>
</html>
