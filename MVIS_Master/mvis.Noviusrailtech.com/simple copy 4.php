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

        .flex-1 {
            width: 250px;
            height: 540px;
            overflow-y: auto;
            padding: 10px;
           /* border-right: 1px solid #ccc;*/
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
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
      
        
        .f1head {
    background:rgb(5 5 5);
    color: rgb(255 255 255);
    padding: 6px;
    text-align: center;
    font-family: 'Rubik', sans-serif;
    font-size: x-small;
    text-transform: uppercase;
    font-weight: bold;
}
        .arrow-down {
            width: 0;
            height: 0;
            border-left: 8px solid transparent;
            border-right: 8px solid transparent;
            border-top: 8px solid black;
            position: absolute;
            top: 50%;
            right: 10px;
            transform: translateY(-50%);
        }
        .dropdown {
            position: relative;
            display: inline-block;
        }

        .dropdown button {
            cursor: pointer;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 135px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }

        .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
        }

        .dropdown-content a:hover {
            background-color: #f1f1f1;
        }

        .dropdown:hover .dropdown-content {
            display: block;
        }
      
        table {
            width: 100%;
            border-collapse: collapse;
        
        }

       
        .f1tab{
        height: 420px;
        }
        .flex-2 {
            width: 1000px;
            overflow-x: auto;
            overflow-y: auto;
            padding: 0px 10px;
            height: 560px;
           
        }

        table {
            width: 100%;
            border-collapse: collapse;
      
        }

       td {
            border: 1px solid #ddd;
            padding: 2px;
            text-align: center;
            font-size: small;
            font-family: 'Rubik', sans-serif;
        }
        th {
            background-color: #375392;
    color: white;
    padding: 5px;
    border: 1px solid #ddd;
    font-size: small;
    font-family: 'Rubik', sans-serif;
}
.t1{
    overflow-y: auto;
}
.t2{
    overflow-y: auto;
}

#tb1 th{
    background-color: #ed2160;
    border: 5px solid #fff;
    color: white;
    padding: 5px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: small;
    font-weight: bold;
}
#tb1 td{
    background-color: #ed2160;;
    border: 1px solid #ddd;
    color: white;
    padding: 5px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: small;
    font-weight: bold;
}
#tb2 th{
    background-color: #f2750f;
    border: 5px solid #fff;
    color: white;
    padding: 5px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: small;
    font-weight: bold;
}
#tb2 td{
    background-color: #f2750f;
    border: 1px solid #ddd;
    color: white;
    padding: 5px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: small;
    font-weight: bold;
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
            overflow-y: auto;
            display: flex;
        }
        .grid-it {
           /* border: 1px solid #ccc;*/
            padding: 20px;
            height: 220px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);    
            display: flex;
            justify-content: center;
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
            font-family: 'Roboto Slab', serif;
            font-family: 'Secular One', sans-serif;
            background-color: rgb(0, 0, 0); color: white; 
            padding: 3px; 
            text-align:center;
            border-top-left-radius: inherit;
            border-top-right-radius: inherit;
            font-size: small;
        }
        #image3 {
            width: 80%;
            height: 100%;
            border-radius: 10px; 
        }
        #textboxes3 {
            width: 30%;
            height: 100%;
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            cursor: pointer;
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
    font-weight: bold;
        }
.bc{
    background-color: black;
    color: #fff;
}
#abc{
    width: 100%;
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
    height: 560px;
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
           font-size: smaller;
           font-weight: bold;
       }

.info{
    display: grid;
           grid-template-columns: repeat(2,1fr);
}
.l1{
        color: black;
       }
       .l3{
        color: rgb(0, 0, 0);
        text-align: center;
       }
  
   
        #image2 {
            width: 90%;
    height: 35px;
    border-radius: 10px 
        }
        #image4 {
            width: 100%;
            height: 58px;
            border-radius: 10px; 
        }
 

        .textbox-container2 {
            position: absolute;
    top: 40%;
    left: 55%;
    transform: translate(-50%, -50%);
    width: 700px;
        }
    
     
  
.footer{
    display: grid;
    grid-template-columns: repeat(3 ,25% 50% 25%);
    background: white;
}
#textboxess {
            width: 100%;
            height: 60px;
            position: relative;
            overflow: hidden;
        }
        #imagex {
            width: 100%;
            height: 58px;
          
        }
        #textboxesss {
            width: 100%;
            height: 60px;
            position: absolute;
            top: 0%;
        }
        #textboxesssm {
            width: 100%;
            height: 60px;
            position: absolute;
            top: 0%;
            display: flex;
            justify-content: center;
        }
        #imagea {
            width: 50%;
            height: 50px;
          
        }
        #imageb {
    width: 8%;
    height: 50px;
   
}
        #imagec {
            width: 50%;
            height: 60px;
            margin-left: 160px; 
        }
        a {
      text-decoration: none;
    }


/* ----------------------------------------------- */
#b3{
    background: #3471be;
    color: #fff;
    width: 30px;
    font-size: medium;
    cursor: pointer;
    height: 30px;
    padding: 5px 4px;
    margin-top: 1px;
}
#b3:hover{
    background:linear-gradient(to top, rgb(1, 71, 193), rgb(81, 125, 244));
}
#texte2 {
    margin-top: 1%;
    margin-left: 50%;
    color: #fff;
    font-size: 45px;
    font-weight: 700;
} 
.right {
    display: flex;
}
a {
      text-decoration: none;
    }
 #texte {
    margin-top: 9px;
    align-items: center;
    color: #fff;
    font-size: 20px; 
    font-weight: 700;
} 
#textboxes1 {
            width: 35px;
            height: 100%;
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            cursor: pointer;
        }   
  .textbox-container1 {
            position: absolute;
            top: 20%;
            left: 34%;
          display: flex;
            width: 100%;
        }
   #textboxes2 {
            width: 100%;
            height: 100%;
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            cursor: pointer;
        }
.textbox-container {
            position: absolute;
            top: 0%;
            /*left: 50%;
            transform: translate(-50%, -50%);*/
            width: 200px;
        }
#image1 {
            width: 100%;
            height: 100%;
     
        }
   #textboxes {
            width: 100%;
            height: 60px;
            position: relative;
            overflow: hidden;
            
        }
        .date{
            background: #dce6f2;
           display: grid;
           padding: 2px;
           border-radius: 2px;
           text-align: justify;
           gap: 4px;
           font-size: x-small;
           font-weight: bold;
         
       }
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
#b1{
    background: #3471be;
    color: #fff;
    width: 100%;
    font-size: medium;
    cursor: pointer;
    height: 27px;
   
}
#b2{
    background:#e6245d;
    color: #fff;
    width: 100%;
    font-size: medium;
    cursor: pointer;
    height: 27px;
}
#b1:hover{
    background:linear-gradient(to top, rgb(1, 71, 193), rgb(81, 125, 244));
}
#b2:hover{
    background:linear-gradient(to top, #d12357, #eb688f);
}

    @media screen and (max-width: 600px) {
    button {
        width: 65px;
    }
    .dropdown-content {
    min-width: 65px;}

    .info {
    display: grid;
    grid-template-columns:1fr;
    gap: 3px;
}
.l3{
    text-align: left;
    }
    #image2 {
            width: 80%;
    height: 30px;
    border-radius: 10px 
        }
        #textboxes1 {
        width: 30px;
            height: 32px;
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            cursor: pointer;
        }
        .textbox-container1 {
    position: absolute;
    top: 58%;
    left: 0%;
    
    width: 500px;
}
        #texte {
    margin-top: 12px;
    align-items: center;
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}
.textbox-container{
            left: 30%;
        }
        #image1 {
            width: 100%;
            height: 120px;
         
        }
        #textboxes {
            width: 100%;
            height: 90px;
            position: relative;
            overflow: hidden;
          
        }
        .textbox-container2 {
    position: absolute;
    top: 40%;
    left: 53%;
    transform: translate(-50%, -50%);
    width: 700px;
}
#imagec {
    width: 70%;
    height: 60px;
    margin-left: 25px;
}
#imagea {
    width: 70%;
    height: 50px;
}
#imageb {
    width: 30%;
    height: 50px;
}
#texte2 {
    margin-top: 10%;
    margin-left: 19%;
    color: #fff;
    font-size: 25px;
    font-weight: 700;
}

nav {
    display: grid;
            justify-content: space-between;
}
}
@media screen and (min-width: 601px) and (max-width: 1023px) {
    button {
        width: 95px;
    }
    .dropdown-content {
    min-width: 95px;
}
    .info {
    display: grid;
    grid-template-columns:1fr;
    gap: 3px;
}
.l3{
    text-align: left;
    }
    #image2 {
            width: 80%;
    height: 30px;
    border-radius: 10px 
        }
        #textboxes1 {
        width: 30px;
            height: 32px;
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            cursor: pointer;
        }
        .textbox-container1 {
    position: absolute;
    top: 58%;
    left: 20%;
    
    width: 500px;
}
        #texte {
    margin-top: 12px;
    align-items: center;
    color: #fff;
    font-size: 12px;
    font-weight: 700;
}
.textbox-container{
            left: 30%;
        }
        #image1 {
            width: 100%;
            height: 100%;
         
        }
        #textboxes {
            width: 100%;
            height: 90px;
            position: relative;
            overflow: hidden;
          
        }
        .textbox-container2 {
    position: absolute;
    top: 40%;
    left: 53%;
    transform: translate(-50%, -50%);
    width: 700px;
}
#imagec {
    width: 70%;
    height: 60px;
    margin-left: 25px;
}
#imagea {
    width: 70%;
    height: 50px;
}
#imageb {
    width: 30%;
    height: 50px;
}
#texte2 {
    margin-top: 5%;
    margin-left: 44%;
    color: #fff;
    font-size: 28px;
    font-weight: 700;
}
.footer {
    display: grid;
    grid-template-columns: repeat(3 ,33% 37% 30%);
}
nav {
    display: grid;
            justify-content: space-between;
}
}

    </style>
</head>
<body>

    <header>
        <div id="textboxes">
            <img id="image1" src="images/21.jpg" alt="Your Image">
            <div class="textbox-container">
                <div id="textboxes2"><img id="image4" src="images/20.png" alt="Second Image">
                </div> 
            </div>

            <div class="textbox-container1">
                <div id="textboxes1"><img id="image2" src="images/1 - Copy.png" alt="Second Image"></div>
                  <div id="texte">
                    NOVIUS MVIS- MACHINE VISION BASED INSPECTION SYSTEM
                </div>
             
                </div> 
            </div>
        <nav>
            <div class="flex-container">
                <button class="save">
                    <div id="textboxes3">
                    <img id="image3" src="images/14.png" alt="Your Image">
                </div>
                
                <a href="index2.html" class="vi" id="videoButton">Control Panel</a>
            </button>
            <button class="save" href="simple.html"style=" background:linear-gradient(to top, rgb(212, 3, 3), rgb(248, 166, 166));">
                <div id="textboxes3">
                <img id="image3" src="images/22 (2).png" alt="Your Image">
            </div>
            <a href="simple.html" class="vi" id="videoButton">Simple View</a>
        </button>
        <button class="save" href="Side.html">
            <div id="textboxes3">
                <img id="image3" src="images/15.png" alt="Your Image">
            </div>
        <a href="Side.html" class="vi" id="videoButton">Side View</a>
    </button>
    <button class="save" href="bogi.html">
        <div id="textboxes3">
            <img id="image3" src="images/19.ico" alt="Your Image">
        </div>
    <a href="bogi.html" class="vi" id="videoButton">Bogi View</a>
</button>
    <button class="save" href="alarm.html">
        <div id="textboxes3">
            <img id="image3" src="images/16.png" alt="Your Image">
        </div>
    <a href="alarm.html" class="vi" id="videoButton">Alaram</a>
</button>
<button class="save">
    <div id="textboxes3">
        <img id="image3" src="images/17.png" alt="Your Image">
    </div>
    <a href="trin.html" class="vi" id="videoButton">Train Summary</a>
</button>
            
                   
                </div>
                <div class="right">
                    <button class="save" id="videoButton">
                        <div id="textboxes3">
                            <img id="image3" src="images/17.png" alt="Your Image">
                        </div>
                        <a href="treport.html" class="vi">Summary Report</a>
                    </button>
                    <div class="dropdown">
                        <button style="border: 0px;font-size: x-small;">CR_PA_MUM-END_2001</button>
                        <div class="dropdown-content">
                            <a href="#">X</a>
                        
                          
                        </div>
                        
                </div>
                <button id="b3"> <i class="fi fi-rr-bell"></i></button> 
                <div class="dropdown">
                    <button style="border: 0px;">Admin<span class="arrow-down"></span></button>
                    <div class="dropdown-content">
                        <a href="#">X</a>
                        <a href="#">Y</a>
                        <a href="#">Z</a>
                        <a href="#">A</a>
                    </div> 
            </div>
    
                    </div>
                    
        </nav>
    </header>

    <div style="height: 10px;"></div>

    <div class="flex-container">
        <div class="flex-1">
            <div class="f1head">TRAIN LOG</div>
            <div class="date">
                <div class="datesub">
            <label for="fromDate">From Date:</label>
            <input type="date" id="fromDate" name="fromDate">
            <label for="toDate">To Date:</label>
            <input type="date" id="toDate" name="toDate">
                </div>
            <div class="button-box">
            <button id="b1">LIVE</button>
            <button id="b2">FILTER</button>
            </div>
            </div>
            <!-- Add 10 rows here -->
            <div class="f1tab"><table>
                <tbody>
                    <!-- Rows -->
                    <tr>
                        <td>Row 1</td>
                    </tr>
                    <tr>
                        <td>Row 2</td>
                    </tr>
                    <tr>
                        <td>Row 3</td>
                    </tr>
                    <tr>
                        <td>Row 4</td>
                    </tr>
                    <tr>
                        <td>Row 5</td>
                    </tr>
                    <tr>
                        <td>Row 6</td>
                    </tr>
                    <tr>
                        <td>Row 7</td>
                    </tr>
                    <tr>
                        <td>Row 8</td>
                    </tr>
                    <tr>
                        <td>Row 9</td>
                    </tr>
                    <tr>
                        <td>Row 10</td>
                    </tr>
                    <tr>
                        <td>Row 11</td>
                    </tr>
                    <tr>
                        <td>Row 12</td>
                    </tr>
                    <tr>
                        <td>Row 13</td>
                    </tr>
                    <tr>
                        <td>Row 14</td>
                    </tr>
                    <tr>
                        <td>Row 15</td>
                    </tr>
                </tbody>
            </table>
        </div>
            
        </div>

        <div class="flex-2">
            <div class="grid-container">
                <!-- Add 7x20 grid items here -->
                <div class="grid-item">
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-1</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-2</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-3</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-4</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-5</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-6</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-7</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-8</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-9</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-10</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-11</div>
                    </button>
                    <button id="abc" class="savess">
                        <div id="textboxes4">

                        </div>
                        <div class="bc">Coach-12</div>
                    </button>
                </div>
<div class="grid-itt">
    <div class="grid-it">


    </div>
                <div class="grid-it">
<div class="t1">
<style>
        table {
            width: 100%;
        }
        th {
            font-size: 10px; /* Adjust the size as needed */
            white-space: pre-line; /* Preserve line breaks */
            word-break: break-all; /* Break words to fit */
        }
        td {
            padding: 8px; /* Adjust padding as needed */
        }
        .auto-width {
            flex: 1;
        }
    </style>
    
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
            <th style="width: 10px">Bolster_Suspension_Hanger</th>
            <th style="width: 10px;">Bolster</th>
            <th style="width: 10px;">Shock_Absorber</th>
            <th style="width: 10px;">Secondary_Suspension</th>
            <th style="width: 10px;">Lower_Spring_Beam</th>
            <th style="width: 10px;">Side_Frame</th>
            <th style="width: 10px;">Brake_Block</th>
               
                
            </tr>
        </thead>
        <tbody>
            <!-- Rows -->
            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['Time_Stamp']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_encode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Primary_Suspension']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_encode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected2.jpg')); ?>')"><?php echo $row['Bolster_Suspension_Hanger']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_encode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected3.jpg')); ?>')"><?php echo $row['Bolster']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_encode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['Shock_Absorber']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_encode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected5.jpg')); ?>')"><?php echo $row['Secondary_Suspension']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_encode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected6.jpg')); ?>')"><?php echo $row['Lower_Spring_Beam']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_encode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected7.jpg')); ?>')"><?php echo $row['Side_Frame']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_encode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected8.jpg')); ?>')"><?php echo $row['Brake_Block']; ?></a></td>


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

    <table>
    <thead>
        
        
        <tr>
        <th style="width: 10px;">Time_Stamp</th>
        <th style="width: 10px;">Primary_Suspension</th>
        <th style="width: 10px">Bolster_Suspension_Hanger</th>
        <th style="width: 10px;">Bolster</th>
        <th style="width: 10px;">Shock_Absorber</th>
        <th style="width: 10px;">Secondary_Suspension</th>
        <th style="width: 10px;">Lower_Spring_Beam</th>
        <th style="width: 10px;">Side_Frame</th>
        <th style="width: 10px;">Brake_Block</th>
           <!-- <th>Axie_Box_Cover</th> -->
            
        </tr>
    </thead>
        <tbody>
            <!-- Rows -->
            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['Time_Stamp']; ?></td>
                        <td><a href="<?php echo $row['Primary_Suspension']; ?>"><?php echo $row['Primary_Suspension']; ?></a></td>
                        <td><a href="<?php echo $row['Bolster_Suspension_Hanger']; ?>"><?php echo $row['Bolster_Suspension_Hanger']; ?></a></td> 
                        <td><a href="<?php echo $row['Bolster']; ?>"><?php echo $row['Bolster']; ?></a></td>
                        <td><a href="<?php echo $row['Shock_Absorber']; ?>"><?php echo $row['Shock_Absorber']; ?></a></td> 
                        <td><a href="<?php echo $row['Secondary_Suspension']; ?>"><?php echo $row['Secondary_Suspension']; ?></a></td> 
                        <td><a href="<?php echo $row['Lower_Spring_Beam']; ?>"><?php echo $row['Lower_Spring_Beam']; ?></a></td>
                        <td><a href="<?php echo $row['Side_Frame']; ?>"><?php echo $row['Side_Frame']; ?></a></td> 
                        <td><a href="<?php echo $row['Brake_Block']; ?>"><?php echo $row['Brake_Block']; ?></a></td> 

                    <!--    <td><?php echo $row['Primary_Suspention']; ?></td>
                      //  <td><?php echo $row['Axie_Box_Cover']; ?></td> -->
                        <!-- Add more columns as needed -->
                    </tr>
                <?php endforeach; ?>
            <?php endif; ?>
</tbody>
</table>

</div>
                </div>
                <div class="grid-it">
                    <div class="t1">
                        <table id="tb1">
                            <thead>
                                <tr>
                                    <th colspan="6">LIST OF ALARAM</th>
                                </tr>
                            
                            </thead>
                            <tbody>
                                <!-- Rows -->
                                <tr>
                                    <td>Axel No</td>
                                    <td>Coach Position</td>
                                    <td>Coach Number</td>
                                    <td>Axel Side</td>
                                    <td>Axel Temp(°C)</td>
                                   
                                </tr> 
                    </tbody>
                    </table>
                    </div>
                    <div class="t1">
                        <table id="tb1">
                            <thead>
                                <tr>
                                    <th colspan="6">LIST OF ALARAM</th>
                                </tr>
                            
                            </thead>
                            <tbody>
                                <!-- Rows -->
                                <tr>
                                    <td>Axel No</td>
                                    <td>Coach Position</td>
                                    <td>Coach Number</td>
                                    <td>Axel Side</td>
                                    <td>Axel Temp(°C)</td>
                                   
                                </tr> 
                    </tbody>
                    </table>
                    </div>
                                    </div>
                                    <div class="grid-it">
                                        <div class="t2">
                                        
                                            <table id="tb2">
                                                <thead>
                                                    <tr>
                                                        <th colspan="6">LIST OF WARNING</th>
                                                    </tr>
                                                   
                                                </thead>
                                                <tbody>
                                                    <!-- Rows -->
                                                    <tr>
                                                        <td>Axel No</td>
                                                        <td>Coach Position</td>
                                                        <td>Coach Number</td>
                                                        <td>Axel Side</td>
                                                        <td>Axel Temp(°C)</td>
                                                    </tr> 
                                        </tbody>
                                        </table>
                                        
                                        </div>
                                        <div class="t2">
                                        
                                            <table id="tb2">
                                                <thead>
                                                    <tr>
                                                        <th colspan="6">LIST OF WARNING</th>
                                                    </tr>
                                                   
                                                </thead>
                                                <tbody>
                                                    <!-- Rows -->
                                                    <tr>
                                                        <td>Axel No</td>
                                                        <td>Coach Position</td>
                                                        <td>Coach Number</td>
                                                        <td>Axel Side</td>
                                                        <td>Axel Temp(°C)</td>
                                                    </tr> 
                                        </tbody>
                                        </table>
                                        
                                        </div>
                                                        </div>


            </div>
        </div>
                <!-- Repeat for 20 rows 
            </div>
            <div class="grid-container">
              Add 2 flex divs with tables here 
                <div class="flex-table">
                    <div>Table Col 1</div>
                    <div>Table Col 2</div>
                    <div>Table Col 3</div>
                    <div>Table Col 4</div>
                    <div>Table Col 5</div>
                    <div>Table Col 6</div>
                </div>
                <div class="flex-table">
                    <div>Table Col 1</div>
                    <div>Table Col 2</div>
                    <div>Table Col 3</div>
                    <div>Table Col 4</div>
                    <div>Table Col 5</div>
                    <div>Table Col 6</div>
                </div>
            </div> -->
        </div>
   
        <div class="flex-3">
            <div class="Tdetail">ARIVAL Date & Time<br>
            2023-12-14 9:30</div>
            <!-- Add 12 rows with 2 flex divs in each row here -->
            <div class="date">
                <div class="info">
                    <div class="l1">Direction</div>
                    <div class="l3">UP</div>   
                </div>
                <div class="info">
                    <div class="l1">Avg. Speed(kmph)</div>
                    <div class="l3">10.6</div>   
                </div>
                <div class="info">
                    <div class="l1">Total No. Of Locos</div>
                    <div class="l3">1</div>   
                </div>
                <div class="info">
                    <div class="l1">Total No. Of Axles</div>
                    <div class="l3">180</div>   
                </div>
                <div class="info">
                    <div class="l1">Total No. Of Coaches/Wagons</div>
                    <div class="l3">21</div>   
                </div>
                <div class="info">
                    <div class="l1">Total No. Of Alarms</div>
                    <div class="l3">0</div>   
                </div>
                <div class="info">
                    <div class="l1">Total No. Of Warning</div>
                    <div class="l3">0</div>   
                </div>
                <div class="info">
                    <div class="l1">Bogi View Components</div>
                    <div class="l3">10</div>   
                </div>
                <div class="info">
                    <div class="l1">Side View Components</div>
                    <div class="l3">10</div>   
                </div>
                <div class="info">
                    <div class="l1">Bottom View Components</div>
                    <div class="l3">10</div>   
                </div><div class="info">
                    <div class="l1">Top View Components</div>
                    <div class="l3">10</div>   
                </div>
                <div class="info">
                    <div class="l1">Max Temp MP(C)</div>
                    <div class="l3">45.76</div>   
                </div>
                <div class="info">
                    <div class="l1">Min Temp MP(c)</div>
                    <div class="l3">27.49</div>   
                </div>
                <div class="info">
                    <div class="l1">Max Temp AP(C)</div>
                    <div class="l3">33.6</div>   
                </div>
                <div class="info">
                    <div class="l1">Min Temp AP(c)</div>
                    <div class="l3">21.49</div>   
                </div>
            </div>
                
            </div>
            <!-- Repeat for 11 more rows -->
        </div>
    </div>
    
   <div class="footer">
        <div class="subfooter">
        <div id="textboxess">
            <img id="imagex" src="images/z.png" alt="Your Image">
            <div id="textboxesss">
                <img id="imagea" src="images/20.png" alt="Your Image">
    
            </div>  
        </div>
        </div>
        <div class="subfooter">
            <div id="textboxess">
                <img id="imagex" src="images/y.png" alt="Your Image">
                <div id="textboxesssm">
                    <img id="imageb" src="images/24.2.png" alt="Your Image">
    
                </div>  
            </div>
            </div>
            <div class="subfooter">
                <div id="textboxess">
                    <img id="imagex" src="images/x.png" alt="Your Image">
                    <div id="textboxesss">
                        <div id="texte2">
                            MVIS
                        </div>
        
                    </div>
                </div>
                </div>
     </div>
     </div>
</body>
</html>
