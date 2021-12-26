#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb
cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()
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

    <h1 class="heading">T A M I L N A D U</h1>

    <div class="box-container">
        <div class="box">
            <img src="images/mat.jpg">
            <div class="content">
                <h3> Meenakshi Amman Temple  </h3>
                <p> Meenakshi Temple is a historic Hindu temple located on the southern bank of the Vaigai River in the temple  city of the Madurai.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                
                <a href="#" class="btn">See Reviews</a>
            </div>
        </div>

        <div class="box">
            <img src="images/dt.jpg">
            <div class="content">
                <h3> Dhanushkodi Beach</h3>
                <p>The town of Dhanushkodi is believed to be the place where Lord Rama had ordered Lord Hanumana to build a bridge which could carry his army across to Sri Lanka.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                
                <a href="#" class="btn">See Reviews</a>
            </div>
        </div>

        <div class="box">
            <img src="images/cwft.jpg">
            <div class="content">
                <h3></i> Courtallam Falls</h3>
                <p>Courtallam fall is the all-time best waterfall in Tamilnadu for tourists. It heights around 550 feet from the ground. Courtallam also pronounced as Kutralam. The water source for the falls is the Chittraru River.  </p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                
                <a href="#" class="btn">See Reviews</a>
            </div>
        </div>

        <div class="box">
            <img src="images/tamilnadu.jpg">
            <div class="content">
                <h3> Brihadeshwara Temple  </h3>
                <p>Brihadeshware temple is the most historical in tamilnadu.The temple has a massive colonnaded prakara (corridor) and one of the largest Shiva lingas in India.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                
                <a href="#" class="btn">See Reviews</a>
            </div>
        </div>


        <div class="box">
            <img src="images/ot.jpg">
            <div class="content">
                <h3>Ooty Hill Station</h3>
                <p>Ooty Hill Station Also known as Udhagamandalam, Ooty is called the 'Queen of hill stations. ' It lies in the Nilgiris at an altitude of 7440ft above sea level..</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                
                <a href="#" class="btn">See Reviews</a>
            </div>
        </div>

        <div class="box">
            <img src="images/gt.jpg">
            <div class="content">
                <h3> Gandhi Museum</h3>
                <p> Gandhi Memorial Museum, established in 1959, is a memorial museum for Gandhi located in the city of Madurai in Tamil Nadu, India. Known as Gandhi Museum.</p>
                <div class="stars">
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="far fa-star"></i>
                </div>
                
                <a href="book.py?rno=%s" class="btn">See Reviews</a>
            </div>
        </div>

    </div>

</section>
<center>
<div class=>
    <input type="submit" class="book"  value="BOOK NOW" onclick="location.href='book.py?rno=%s';">
</div> 
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

</body>
</html>
"""%(rno,rno,rno,rno,rno,rno,rno))