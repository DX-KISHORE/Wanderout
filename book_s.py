#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb
cgitb.enable()

f = cgi.FieldStorage()
rno = f.getvalue("rno")


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css" />
    <title>Wanderout</title>
    <link rel="stylesheet" href="s3.css">

</head>
<body>


        <div class="navbar">
            <div>
                <a href='#'>WANDER OUT</a>
            </div>
            <nav>
                <ul id='MenuItems'>
                    <li><a href='home.py?rno=%s'>Home</a></li>
                    <li><a href='places.py?rno=%s'>Places</a></li>
                    <li><a href='b_login.py?rno=%s'>Booking Status</a></li>
                     <li><a href='review.py?rno=%s'>Reviews</a></li>
                    <li><a href='contact.py?rno=%s'>Contact</a></li>
                    <li><button class='loginbtn' onclick="location.href='home.py';">Logout</button></li>
                </ul>
            </nav>
        </div>
<center>
    <form>
               <h1 class="heading">SAVED SUCESSFULLY</h1>
                <input type="submit" class="btn" value="View" name="sub" onclick="location.href='mybooking.py?rno=%s';"/>

    </form>           
    </center>
    <div class="footer">
        <div class="box-container">
            <div class="box">
                <h3>About us</h3>
                <p>Have a Wonderful Journey fgfhgjbklmkbchjklkkkkkkkkkk</p>
            </div>
            <div class="box">
                <h3>Branch locations</h3>
                <a href="#">India</a>
                <a href="#">USA</a>
                <a href="#">Japan</a>
                <a href="#">France</a>
            </div>
            <div class="box">
                <h3>Quick links</h3>
               <a href="home.py">Home</a>
                <a href="places.py">Places</a>
                <a href="mybooking.py">My Booking</a>
                <a href="review.py">Review</a>
                <a href="contact.py">Contact</a>
            </div>
            <div class="box">
                <h3>Follow us</h3>
                <a href="#">facebook</a>
                <a href="#">instagram</a>
                <a href="#">twitter</a>
                <a href="#">linkedin</a>
            </div>
        </div>
            <h1 class="credit"> created by <span> KMS TEAM </span> | all rights reserved! </h1>
</div>


""" %(rno,rno,rno,rno,rno,rno))
