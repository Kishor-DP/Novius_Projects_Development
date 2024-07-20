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
            width: 1%;
        }

       td {
            border: 1px solid #ddd;
            padding: 2px;
            text-align: center;
            font-size: xx-small;
            fon
            t-family: 'Rubik', sans-serif;
        }

        table #tb0{
            width:400px ;
        }
       #tb0 th{
            background-color: #375392;
    color: white;
    padding: 0px;
    border: 1px solid #ddd;
    font-size: xx-small;
    font-family: 'Rubik', sans-serif;
width: 70px;
}

.t1{
    overflow-y: auto;
    width: -webkit-fill-available;
}
.t2{
    overflow-y: auto;
    width: -webkit-fill-available;
}

#tb1 th{
    background-color: #ed2160;
  
    color: white;
    padding: 0px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: xx-small;
    font-weight: bold;
    width: 70px;
}
#tb1 td{
    
    border: 1px solid #ddd;
  
    padding: 0px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: xx-small;
    
}
#tb2 th{
    background-color: #f2750f;
    width: 70px;
    color: white;
    padding: 0px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: xx-small;
    font-weight: bold;
}
#tb2 td{
   
    border: 1px solid #ddd;
  
    padding: 0px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: xx-small;
    
}


#tb6 th{
    background-color: #0f2df2;
    /* width: 70px; */
    color: white;
    padding: 2px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: x-small;
    font-weight: bold;
}
#tb6 td{
   
    border: 1px solid #ddd;
    padding: 0px;
    border-collapse: separate;
    font-family: 'Rubik', sans-serif;
    font-size: xx-small;
    
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
            padding: 5px;
            height: 67px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);    
            display: flex;
            justify-content: space-between;
            gap: 20px;
            background-repeat: no-repeat;
            background-position: center;
            background-size: contain;
        }
        .grid-itfrst {
           /* border: 1px solid #ccc;*/
            padding: 5px;
            height: 125px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);    
            display: flex;
            justify-content: space-between;
            gap: 20px;
            background-repeat: no-repeat;
            background-position: center;
            background-size: contain;
        }
        .grid-itsnd {
            padding: 5px;
    height: 360px;
    background-color: #fff;
    border-radius: 0px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    display: flex;
    justify-content: space-between;
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
    background-image: url('images/Screenshot 2024-04-08 121525.png');
    background-size: 100% 100%;
}

.savess-coach-0 {
    background-image: url('images/Screenshot 2024-04-10 115330.png'); /* Background image for Coach-0 button */
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
    width: clamp(40px, 54px, 70px);
    font-size: clamp(8px, 10px, 12px);
    cursor: pointer;
    height: 20px;
    border-radius: 8px;
   
}
#b2{
    background:#e6245d;
    color: #fff;
    width: clamp(40px, 54px, 70px);
    font-size: clamp(8px, 10px, 12px);
    cursor: pointer;
    height: 20px;
    border-radius: 8px;
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
            height: 150px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);    
            display: flex;
            justify-content: space-between;
            gap: 20px;
            overflow-x: auto;

        }
        .left-column121, .right-column121 {
      width:-webkit-fill-available;
      display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3px;
    }

    .image-box121 {
      height: 45px;
      width: 100%;
      margin-bottom: 5px;
      background-size: cover;
      background-position: center;
      border: 1px solid black;
    }
        .fst-grid {
    height: 40px;
    background-color: #fff;
    /* border-radius: 8px; */
    /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); */
    /* overflow-y: auto; */
    display: grid;
    background: linear-gradient(to top, rgb(3, 3, 3), rgb(108, 109, 109));
    grid-template-columns: 82% 18%;
}
.fst-grid2{
    display: grid;
    justify-content: center;
    margin-top: 3px;
}
.subbb{
    display: flex;
    justify-content: center;
    margin-left: 18%;
}
.subbb1{
    display: flex;
    justify-content: space-between;
}
.subbb2{
   
    font-family: 'Rubik', sans-serif;
    font-size: small;
    text-transform: uppercase;
    font-weight: bold;
    color: white;
    margin-left: 100px;

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

.scroll-container {
      position: relative;
      width: 900px; /* Adjust the width as needed */
      overflow: hidden;
    }

    .scroll-content {
      display: flex;
      transition: transform 0.5s ease;
    }
    .scroll-button {
      position: relative;
      background-color: #3498db;
      color: #fff;
      border: none;
      padding: 10px;
      cursor: pointer;
      width: min-content;
    }

    .scroll-button.left {
      left: 0;
    }

    .scroll-button.right {
      right: 0;
    }
/* ---------------new table backlinking------------------ */
.code-grid {
 
    margin: 0px 3px;
    border: 1px solid #eaeaea;
    padding: 0px;
    cursor: pointer;
    font-size: xx-small; /* Add cursor pointer to indicate clickable */
    /* background-color: lightcyan; */
    display: grid;
    justify-content: ;

  }
  .code-grid:hover {
    background-color: #6dffff; /* Change this to the desired hover color */
}

/* Define styles for active state */

.code-grid.active {
    background-color: #dcdcdc; /* Change this to the desired active color */
    color: white;
}

  .code-grids-container {
    display: grid;
    height: 425px;
    overflow-x: scroll;
  }

.traname {
    font-size: x-small;
    font-family: Rubik, sans-serif;
    padding: 4px;
}
#tb3{
    height: 500px;
}
#tb3 td{
    font-size: small;
    border: none;
}
#tb3 th{
    text-align: left;
}
#imageaa3 {
    width: 100%;
    height: 76%;
    object-fit: cover;
}
#textboxes111 {
    /* width: 35px; */
    height: 100%;
    position: relative;
    overflow: hidden;
    cursor: pointer;
}
#textboxes112 {
    /* width: 35px; */
    height: 100%;
    position: relative;
    overflow: hidden;
    cursor: pointer;
}
.text-below {
    font-size: xx-small;
    text-align: center;
    color: #333;
    font-weight: 800;
}
/* --------------------------------image hover------------------------------------- */
.left-column121#textboxes111:hover {
transform: scale(1.1, 1.1);
}
.left-column121:hover #textboxes111:not(:hover) {
filter: blur(8px);
transform: scale(0.9, 0.9);
}

.right-column121#textboxes111:hover {
transform: scale(1.1, 1.1);
}
.right-column121:hover #textboxes111:not(:hover) {
filter: blur(8px);
transform: scale(0.9, 0.9);
}
/* -------------------video------------ */
video {
        width: 100%;
        height: 100%;
        margin-bottom: 0px;
        object-fit: cover;
    }
    .videoshow{
        height: 60px;
    }
    /* ---------------------------train sub grid----------------- */
    .coach-id-container {
    display: flex;
    flex-wrap: wrap; /* Allow items to wrap to the next row */
    gap: 5px; /* Adjust the gap between coach IDs as needed */
}

.coach-id-box {
    border: 1px solid #000;
    padding: 10px;
    text-align: center;
    min-width: 100px; /* Set a minimum width for each coach ID box */
    background-image: url('images/Screenshot 2024-04-08 121525.png');
    background-size: 100% 100%;
}

  /* ------------------------------------- */
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
     <script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
  <script>
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
            <div id="code-grids-container" style=" display: grid;
    height: 425px;
    overflow-x: scroll;"></div>
            
        </div>

        <div class="flex-2">
            <div class="grid-container">
            <div class="fst-grid">
            <div class="fst-grid1">
            <div class="subbb">
                        <div class="subbb3">Mvis Simple View</div>
                        <!-- <div class="subbb3"> <input type="number" id="coachInput" placeholder="Coach Position" oninput="addCoaches()"> </div> -->
                    </div>
<div class="subbb1">
    <div class="subbb2">Left Hand Side View</div>
    <div class="subbb2">Right Hand Side View</div>
</div>
            </div>
            <div class="fst-grid2">
 <input type="number" id="coachInput" placeholder="Coach Position" oninput="addCoaches()" style="height: 10px;"> 
 <select id="uniqueNames">
 <option value="" disabled selected>Coach Number</option>
 <option value="name2">1</option>
  <option value="name3">2</option>
  <option value="name2">3</option>
  <option value="name3">4</option>
  <option value="name2">5</option>
  <option value="name3">6</option>
  <option value="name2">7</option>
  <option value="name3">8</option>
</select>
            </div>       
</div>
                <!-- Add 7x20 grid items here -->
                <div class="grid-item" id="gridContainer">
              
                <button class="scroll-button left">&larr;</button>
  <div class="scroll-container">
    <div id="scroll-content">
      <!-- Your content goes here -->
      <button class="savess savess-coach-0">
        <div id="textboxes4"></div>
        <div class="bc">Coach-0</div>
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
      <!-- Repeat the pattern for more items -->
    </div>
  </div>
  <button class="scroll-button right">&rarr;</button>
                </div>
<div class="grid-itt">
<div class="grid-itfst">
        <div class="left-column121">
        <div id="textboxes112">
        
        <div class="videoshow"><video id="video1" controls muted loop src="images/wagon.mp4" alt="Video 1"></video></div>
        <div class="text-below">LH SIDE VIEW VIDEO</div>
        </div>
        <div id="textboxes111">
        
        <img class="image-popup" id="imageaa3" src="images/wagon.png" alt="Video 1">
        <div class="text-below">LH SIDE VIEW IMAGE</div>
        </div>
        <div id="textboxes112">
        
        <div class="videoshow"><video id="video2" controls muted loop src="images/WAGAN2.mp4" alt="Video 2"></video></div>
        <div class="text-below"> LH SIDE VIEW VIDEO</div>
        </div>
        <div id="textboxes111">
        
        <img class="image-popup" id="imageaa3" src="images/wagon2.png" alt="Video 1">
        <div class="text-below">LH SIDE VIEW IMAGE</div>
        </div>
          </div>
          <div class="right-column121">
          <div id="textboxes112">
          <div class="videoshow"><video id="video3" controls muted loop src="images/WAGAN3.mp4" alt="Video 3"></video></div>
          <div class="text-below"> RH SIDE VIEW VIDEO</div>
          </div>
          <div id="textboxes111">
          <img class="image-popup" id="imageaa3" src="images/wagon3.png" alt="Video 1">
          <div class="text-below">RH SIDE VIEW IMAGE</div>
          </div>
            <div id="textboxes112">
            <div class="videoshow"><video id="video4" controls muted loop src="images/WAGAN4.mp4" alt="Video 4"></video></div>
            <div class="text-below"> RH SIDE VIEW VIDEO</div>
        </div>
            <div id="textboxes111">
            <img class="image-popup" id="imageaa3" src="images/wagon4.png" alt="Video 1">
            <div class="text-below">RH SIDE VIEW IMAGE</div>
            </div>
          </div>
        </div>
        
        <div id="image-popup-container" class="popup-container">
  <span class="close" onclick="closePopup()">&times;</span>
  <img id="popup-image" src="" alt="Popup Image">
  <div id="popup-title" class="title"></div> <!-- Container for the title -->
  <button onclick="closePopup()">Close</button>
</div>


<style>
  /* CSS for Popup Window */
  .popup-container {
    display: none;
    position: fixed;
    z-index: 9999;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.7);
  }

  .popup-container img {
    display: block;
    margin: auto;
    max-width: 80%;
    max-height: 70%;
    margin-top: 50px;
  }

  .popup-container button {
    display: block;
    margin: auto;
    margin-top: 20px;
    padding: 10px 20px;
  }

  .popup-container .close {
    color: #fff;
    position: absolute;
    top: 20px;
    right: 30px;
    font-size: 30px;
    cursor: pointer;
  }

  #popup-title {
    background-color: white;
    text-align: center;
    padding: 10px;
    margin-top: 10px;
    font-weight: 700;
  }
</style>

<script>
  // JavaScript for Image Popup
  const imagePopups = document.querySelectorAll('.image-popup');
  const popupContainer = document.getElementById('image-popup-container');
  const popupImage = document.getElementById('popup-image');
  const popupTitle = document.getElementById('popup-title');

  imagePopups.forEach(image => {
    image.addEventListener('click', () => {
      popupImage.src = image.src;
      // Fetching the title from the associated text-below div
      popupTitle.innerText = image.parentNode.querySelector('.text-below').innerText;
      popupContainer.style.display = 'block';
    });
  });

  function closePopup() {
    popupContainer.style.display = 'none';
  }
</script>




        <div class="grid-itfrst">
                                        <div class="t2">
                                        
                                            <table id="tb6">
                                            <?php
       $host = '103.120.176.21';
       $dbname = 'noviusr1_HAHW';
       $username = 'noviusr1_novius2';
       $password = 'Yoj9IbR0y#M%';
        
        try {
            $conn = new PDO("sqlsrv:Server=$host;Database=$dbname", $username, $password);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Prepare the SQL query
            $stmt = $conn->prepare("SELECT * FROM tblTemperatureLog");
            
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
                                    <th>Axle No</th>
                                    <th>Coach Position</th>
                                    <th>Coach Number</th>
                                    <th>MP Axle Temp</th>
                                    <th>Ap Axle Temp</th>
                                    <th>MP Wheel Temp</th>
                                    <th>Ap Wheel Temp</th>
                                    <th>MP Brake Disc Temp</th>
                                    <th>AP Brake Disc Temp</th>
                                </tr>
                            
                            </thead>
                            <tbody>

                            <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                  
                 
                   <tr>
                        <td><?php echo $row['intAxleNo']; ?></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['IntCoachPosition']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected2.jpg')); ?>')"><?php echo $row['NvcharCoachNo']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected3.jpg')); ?>')"><?php echo $row['decTs1']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['decTs2']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['decTs3']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['decTs4']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['decTs5']; ?></a></td>
                        <td><a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected4.jpg')); ?>')"><?php echo $row['decTs6']; ?></a></td>

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

                <div class="grid-itsnd">
<div class="t1">
<style>
    #tb5{
            width: 100%;
            
        }
        #tb5 th {
        display: none;
    }
        td {
         
        }
        .auto-width {
            flex: 1;
        }
    </style>
    
    <table id="tb0">
  <thead>
    <tr>
      <th>Sr No</th>
      <th>Code</th>
      <th>Component</th>
      <th>Parameter</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <!-- Alert data will be inserted here dynamically -->
  </tbody>
</table>
<script>
  // Function to fetch JSON data and create grids
  function fetchDataAndCreateGrids() {
    fetch('fetch_data.php') // Assuming your PHP script is named fetch_data.php
      .then(response => response.json())
      .then(data => {
        createGrids(data);
      })
      .catch(error => console.error('Error fetching data:', error));
  }

  // Function to create grids and attach event listeners
  function createGrids(jsonData) {
    var container = document.getElementById('code-grids-container');
    var tableBody = document.querySelector('#tb0 tbody');
    var uniqueCodes = [];

    // Extract unique codes
    jsonData.forEach(function(item) {
      if (uniqueCodes.indexOf(item.Code) === -1) {
        uniqueCodes.push(item.Code);
      }
    });

    // Create grids for each unique code
    uniqueCodes.forEach(function(code) {
      var gridDiv = document.createElement('div');
      gridDiv.classList.add('code-grid');
      // Find the corresponding timestamp for the code
      var timeStamp;
      jsonData.forEach(function(item) {
        if (item.Code === code) {
          timeStamp = item.Time_Stamp_Gridviewtbl;
        }
      });
      gridDiv.innerHTML = '<div class=traname>' + timeStamp + '</div>';

      // Attach click event listener
      gridDiv.addEventListener('click', function() {
        sendDataToServer(code, tableBody);
        sendCoachDataToServer(code); // Call function to fetch and display coach data
      });
      container.appendChild(gridDiv);
    });
  }

  // Function to send data to server
  function sendDataToServer(code, tableBody) {
    fetch('send_data.php?code=' + encodeURIComponent(code))
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        showDataInGrid(data, tableBody);
      })
      .catch(error => console.error('Error sending data to server:', error));
  }

  // Function to send data to server and display coach data
  function sendCoachDataToServer(code) {
    fetch('coachdata.php?code=' + encodeURIComponent(code))
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        displayCoachData(data);
      })
      .catch(error => console.error('Error sending coach data to server:', error));
  }

  // Function to show alert data in the specified table container
  function showDataInGrid(data, tableBody) {
    // Clear previous data
    tableBody.innerHTML = '';

    // Populate table rows with received data
    data.forEach(function(rowData, index) {
      var row = document.createElement('tr');
      row.innerHTML = `
        <td>${index + 1}</td>
        <td>${rowData.Code}</td>
        <td>${rowData.Component}</td>
        <td>${rowData.Parameter}</td>
        <td>${rowData.Status}</td>
      `;
      tableBody.appendChild(row);
    });
  }

 // Function to display coach data in the specified container
function displayCoachData(data) {
    // Assuming you have a container with id 'scroll-content' to display the coach data
    var container = document.getElementById('scroll-content');
    container.innerHTML = ''; // Clear previous data

    // Create a div element to contain the coach IDs
    var coachIdContainer = document.createElement('div');
    coachIdContainer.classList.add('coach-id-container');

    // Populate coach ID container with coach IDs
    data.forEach(function(rowData) {
        var coachIdBox = document.createElement('div');
        coachIdBox.classList.add('coach-id-box');
        coachIdBox.textContent = rowData.CoachId;

        // Add click event listener to coach ID box
        coachIdBox.addEventListener('click', function() {
            sendCoachIdToServer(rowData.CoachId);
        });

        coachIdContainer.appendChild(coachIdBox);
    });

    container.appendChild(coachIdContainer);
}

// Function to send coach ID to server and display data in #tb0 tbody
function sendCoachIdToServer(coachId) {
    fetch('sendcoach.php?CoachId=' + encodeURIComponent(coachId)) // Ensure 'CoachId' matches PHP parameter
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            showDataInGrid(data, document.querySelector('#tb0 tbody'));
        })
        .catch(error => console.error('Error sending coach ID to server:', error));
}

  // Call the function to fetch data and create grids
  fetchDataAndCreateGrids();
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
                                    <th>Sr No</th>
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
                                    <th>Sr No</th>
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
                                    <th>Sr No</th>
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
                                    <th>Sr No</th>
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
                 
    <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Direction']; ?></a></td>
    <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Avg Speed (Kmph)</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Avg_Speed(Kmph)']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Total No Of Locos</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Total_No_Of_Locos']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Total No Of Axles</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Total_No_Of_Axles']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>No Of Coaches /Wagons</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
                    <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['No_Of_Coaches/Wagons'];?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Total No Of Alarms</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Total_No_Of_Alarms']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Total No Of Warning</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Total_No_Of_Warning']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Bogie View Components</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Bogie_View_Components']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>
        </tr>
  <tr>
    <th>Side View Components</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Side_View_Components']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>
        </tr>
  <tr>
    <th>Bottom Components</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Bottom_Components']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>Top View Components</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['Top_View_Components']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>MaxTemp MP</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MaxTemp_MP']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>MinTemp MP</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
   <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MinTemp_MP']; ?></a></td>
   <?php endforeach; ?>
            <?php endif; ?>  
</tr>
  <tr>
    <th>MaxTemp AP</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
    <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MaxTemp_AP']; ?></a></td>
  
    <?php endforeach; ?>
            <?php endif; ?>
        </tr>
  <tr>
    <th>MinTemp AP</th>
    <?php if (!empty($rows)): ?>
                <?php foreach ($rows as $row): ?>
    <td> : <a href="#" onclick="showImage('<?php echo 'data:image/jpeg;base64,' . base64_enCode(file_get_contents('D:/A RAIL/cloud/1/mvis.Noviusrailtech.com/ftp/pune_mum_end/detected1.jpg')); ?>')"><?php echo $row['MinTemp_AP']; ?></a></td>
  
    <?php endforeach; ?>
            <?php endif; ?>
        </tr>
          
             
</tbody>
</table>
<script>
        function showImage(imageUrl) {
            document.querySelector('.grid-it').style.backgroundImage = 'url("' + imageUrl + '")';
        }
       
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
</body>
</html>
