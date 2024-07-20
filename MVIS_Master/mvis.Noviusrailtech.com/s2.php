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

        .flex-1 {
            width: 250px;
            height: 540px;
            overflow-y: auto;
           
           /* border-right: 1px solid #ccc;*/
            background-color: #fff;
         
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
            overflow-y: auto;
            display: flex;
            width: 960px;
    overflow-x: scroll;
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
           font-size: small;
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
.grid-itfst {
           /* border: 1px solid #ccc;*/
            padding: 10px;
            height: 200px;
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
.info2 {
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
.grid-item {
    width: 100%;
}
    }
@media screen and (min-width: 601px) and (max-width: 1023px) {
    .grid-item {
    width: 100%;
}
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
.info2 {
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
    <a href="alarm.html" class="vi" id="videoButton">Alarm</a>
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
      
            <button id="b2">FILTER</button>
            <button id="b1">LIVE</button>
            </div>
            </div>
            <!-- Add 10 rows here -->
            <div class="f1tab"><table id="tb5">
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
       $username = 'noviusr1_pune_mum_end';
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
                                    <th>MP_side_Axle_Temp(°C)</th>
                                    <th>Ap_side_Axle_Temp(°C)</th>
                                    <th>Wheel_Temp</th>
                                   
                                </tr>
                            
                            </thead>
                            <tbody>

                            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['Axle_No']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Coach_Position']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected2.jpg')); ?>')"><?php echo $row['MP_side_Axle_Temp(°C)']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected3.jpg')); ?>')"><?php echo $row['Ap_side_Axle_Temp(°C)']; ?></a></td>
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
       $username = 'noviusr1_pune_mum_end';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM MVIS_left");
            
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
       $username = 'noviusr1_pune_mum_end';
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
       $username = 'noviusr1_pune_mum_end';
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
       $username = 'noviusr1_pune_mum_end';
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
       $username = 'noviusr1_pune_mum_end';
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
       $username = 'noviusr1_pune_mum_end';
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
       $username = 'noviusr1_pune_mum_end';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM Train_Details");
            
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
    <th>MaxTemp_MP(°C)</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MaxTemp_MP(°C)']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>MinTemp_MP(°C)</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MinTemp_MP(°C)']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>MaxTemp_AP(°C)</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
    <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MaxTemp_AP(°C)']; ?></a></td>
  
    <?php endforeach; ?>
            <?php endif; ?>
        </tr>
  <tr>
    <th>MinTemp_AP(°C)</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
    <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MinTemp_AP(°C)']; ?></a></td>
  
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






    function createButtons() {
        <?php if (!empty($rows)): ?>
            <?php foreach ($rows as $row): ?>
                var numberOfCoaches = <?php echo $row['No_Of_Coaches/Wagons']; ?>;
                if (!isNaN(numberOfCoaches) && numberOfCoaches > 0) {
                    for (var i = 1; i <= numberOfCoaches; i++) {
                        var newButton = document.createElement("button");
                        newButton.id = "abc";
                        newButton.className = "savess";

                        var textboxesDiv = document.createElement("div");
                        textboxesDiv.id = "textboxes4";

                        var coachNameDiv = document.createElement("div");
                        coachNameDiv.className = "bc";
                        coachNameDiv.innerHTML = "Coach-" + i;

                        newButton.appendChild(textboxesDiv);
                        newButton.appendChild(coachNameDiv);

                        var gridContainer = document.getElementById("gridContainer");
                        gridContainer.appendChild(newButton);
                    }
                }
            <?php endforeach; ?>
        <?php endif; ?>
    }

</script>

</body>
</html>
