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
    <link rel="stylesheet" href="style_2.css">
   
</head>

<body>
<div class="navbar">
            <div>
                <a href='website.html'>WANDER OUT</a>
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
        
<section class="places">

    <h1 class="heading">P L A C E S</h1>

    <div class="box-container">
        <div class="box">
            <img src="images/tamilnadu.jpg">
            <div class="content">
                <h3> TAMILNADU </h3>
                <p>Tamilnadu attracts tourists from other Indian states and foreign countries. It was the first most visited state by foreigners.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                <div class="price"> Rs.10,000 Only</div>
                <a href="tamilnadu.py?rno=%s" class="btn">See more</a>
            </div>
        </div>
        
        <div class="box">
            <img src="images/kerala.jpg">
            <div class="content">
                <h3> KERALA </h3>
                <p>Kerala is also known as "God's Own Country" and Is famous for its ecotourism initiatives and beautiful backwaters.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                <div class="price"> Rs.7,000 Only </div>
                <a href="#" class="btn">See more</a>
            </div>
        </div>

        <div class="box">
            <img src="images/kar.jpg">
            <div class="content">
                <h3></i> KARNATAKA</h3>
                <p>Karnataka, the sixth largest state in India, has been ranked as the third most popular state in the country for tourism in 2014. </p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                <div class="price"> Rs.8,000 Only</div>
                <a href="#" class="btn">See more</a>
            </div>
        </div>

        <div class="box">
            <img src="images/mumbai.jpg">
            <div class="content">
                <h3>  MAHARASHTRA </h3>
                <p>Maharashtra attracts tourists from other Indian states and foreign countries. It was the second most visited state by foreigners and fourth most visited state by domestic tourists in the country.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                <div class="price"> Rs.12,000 Only </div>
                <a href="#" class="btn">See more</a>
            </div>
        </div>

        
        <div class="box">
            <img src="images/jk.jpg">
            <div class="content">
                <h3>JAMMU/KASHMIR</h3>
                <p>Jammu and Kashmir is also famous for its scenic beauty, flower gardens, apple farms and more. It attracts tourists for its unique handicrafts and the world-famous Kashmiri Shawls.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                <div class="price"> Rs.10,000 Only</div>
                <a href="#" class="btn">See more</a>
            </div>
        </div>
        
        <div class="box">
            <img src="images/Goa.jpg">
            <div class="content">
                <h3> GOA</h3>
                <p> The state of Goa, in India, is famous for its beaches and places of worship.Major tourist attractions include Bom Jesus Basilica, Fort Aguada, a wax museum , and a heritage museum.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                <div class="price"> Rs.10,000 Only</div>
                <a href="#" class="btn">See more</a>
            </div>
        </div>

    </div>

</section>

<!-- places section ends -->
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
        
</body>
</html>
"""%(rno,rno,rno,rno,rno,rno))