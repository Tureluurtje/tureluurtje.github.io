<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webshop</title>
    <style>
        body {
            font-family: Lato, sans-serif;
            margin: 0;
            padding: 0;
            color: #DFDBD8;
            transition: 5s;
            text-align: left;
        }

        header {
            background-color: #565C5E;
            color: #fff;
            padding: 10px;
            text-align: center;
        }

        h1 {
            margin: 0;
            text-align: left;
        }

        .container {
            max-width: 960px;
            margin: 20px auto;
            padding: 0 20px;
            text-align: left;
        }

        .product {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 20px;
            transition-duration: 0.3s;
            cursor: pointer;
            text-align: left;
        }
        .product1{
            background-color:white;
            color: black;
            border: none;
        }
        .product1:hover{
            background-color:#B5C2C7 ;
            color: black;
        }

        .product h3 {
            margin: 0;
        }

        .product p {
            margin: 10px 0;
        }

        footer {
            background-color: #f4f4f4;
            padding: 10px;
            text-align: center;
        }
        button {
            border: none;
            color: black;
            padding: 8px 16px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            transition-duration: 0.3s;
            cursor: pointer;
            border-radius: 16;
        }
        .button1 {
            background-color:white;
            color: black;
            border: 2px solid rgb(218, 165, 32);
        }
        .button1:hover {
            background-color: rgb(218, 165, 32);
            color: white;
        }

    	.sidenav {
            height: 100%;
            width: 0;
            position: fixed;
            z-index: 1;
            top: 0;
            left: 0;
             background-color: #111;
            overflow-x: hidden;
            transition: 0.5s;
            padding-top: 60px;
        }

        .sidenav a {
            padding: 8px 8px 8px 32px;
            text-decoration: none;
            font-size: 25px;
            color: #818181;
            display: block;
            transition: 0.3s;
        }

        .sidenav a:hover {
           color: #f1f1f1;
        }

        .sidenav .closebtn {
             position: absolute;
             top: 0;
             right: 25px;
            font-size: 36px;
             margin-left: 50px;
        }

        #main {
             transition: margin-left .5s;
                 padding: 16px;
        }

        @media screen and (max-height: 450px) {
            .sidenav {padding-top: 15px;}
            .sidenav a {font-size: 18px;}
        }
        </style>
</head>
<body>
    <header>
        <h1>Producten</h1>
    </header>
<div id="mySidenav" class="sidenav">
    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
    <a href="#">About</a>
    <a href="#">Services</a>
    <a href="#">Clients</a>
    <a href="#">Contact</a>
</div>
    <div id="main" class="container">
        <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; open</span>
        <div class="product product1">
            <h3>Storage Hell</h3>
            <h5>dumps unlimited random files in storage of the target.</h5>
            <p>Price: €9.99</p>
            <button class="button button1">Add to Cart</button>
        </div>

        <div class="product product1">
            <h3>Product 2</h3>
            <p>Price: $19.99</p>
            <button class="button button1">Add to Cart</button>
        </div>

        <div class="product product1">
            <h3>Product 3</h3>
            <p>Price: $29.99</p>
            <button class="button button1">Add to Cart</button>
        </div>
    </div>
    <script>
        function openNav() {
            document.getElementById("mySidenav").style.width = "250px";
            document.getElementById("main").style.marginLeft = "250px";
            document.body.style.backgroundColor = "white";
        }

        function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
        document.getElementById("main").style.marginLeft= "0";
        document.body.style.backgroundColor = "white";
        }
    </script>

    <footer>
        &copy; 2021 Webshop. All rights reserved.
    </footer>
</body>
</html>
