#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb
cgitb.enable()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css">
    <title>Wanderout</title>
    <link rel="stylesheet" href="style4.css">
    
</head>
<body>

<div class="navbar">
            <div>
                <a href='website.html'>WANDER OUT</a>
            </div>
            <nav>
                <ul id='MenuItems'>
                    <li><a href='home.py'>Home</a></li>
                    <li><a href='places.py'>Places</a></li>
                    <li><a href='mybooking.py'> My Booking</a></li>
                     <li><a href='review.py'>Reviews</a></li>
                    <li><a href='contact.py'>Contact</a></li>
                    <li><button class='loginbtn' onclick="location.href='login.py';">Login</button></li>
                </ul>
            </nav>
        </div>
<center>
<section class="places">

    <h1 class="heading">R E V I E W S</h1>

    <div class="box-container">
        <div class="box">
            <img src="images/r1.jpg">
            <div class="content">
                <h3> Mariya Amali </h3>
                <p> Meenakshi Temple is a historic Hindu temple located on the southern bank of the Vaigai River in the temple  city of the Madurai.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
            </div>
        </div>
    
        <div class="box">
            <img src="images/r2.jpg">
            <div class="content">
                <h3> Jhon Wick</h3>
                <p>The town of Dhanushkodi is believed to be the place where Lord Rama had ordered Lord Hanumana to build a bridge which could carry his army across to Sri Lanka.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>

                
            </div>
        </div>

        <div class="box">
            <img src="images/r3.jpg">
            <div class="content">
                <h3></i> Harry potter</h3>
                <p>Courtallam fall is the all-time best waterfall in Tamilnadu for tourists. It heights around 550 feet from the ground. Courtallam also pronounced as Kutralam. The water source for the falls is the Chittraru River.  </p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>

                
            </div>
        </div>

        <div class="box">
            <img src="images/r4.jpg">
            <div class="content">
                <h3> Priyanka </h3>
                <p>Brihadeshware temple is the most historical in tamilnadu.The temple has a massive colonnaded prakara (corridor) and one of the largest Shiva lingas in India.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>

                
            </div>
        </div>


        <div class="box">
            <img src="images/r5.jpg">
            <div class="content">
                <h3>Dx Hacker</h3>
                <p>Ooty Hill Station Also known as Udhagamandalam, Ooty is called the 'Queen of hill stations. ' It lies in the Nilgiris at an altitude of 7440ft above sea level..</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>

                
            </div>
        </div>

        <div class="box">
            <img src="images/r6.jpg">
            <div class="content">
                <h3> Harish</h3>
                <p> Gandhi Memorial Museum, established in 1959, is a memorial museum for Gandhi located in the city of Madurai in Tamil Nadu, India. Known as Gandhi Museum.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>

                
            </div>
        </div>

    </div>

</section>
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
                <a href="book.py">Booking</a>
                <a href="services.py">Services</a>
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
""")