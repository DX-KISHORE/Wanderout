#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb
cgitb.enable()

f = cgi.FieldStorage()
rno = f.getvalue("rno")

conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()

#q = """select fullname from customer where coustid='%s' """%(rno)
#cur.execute(q)

#r = cur.fetchone()
#print(r)





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
    <link rel="stylesheet" href="style1.css">
</head>
<body>

        <div class="navbar">
            <div>
                <a>WELCOME %s</a>
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

    <div class="full-page">
    
    <section>
    
    <div class="content">
        
        <h3>Adventure is Worthwhile</h3>
        <p>Discover new places with us, Adventure awaits</p>    
        <div class="search">
            <input type="text" name="" class="query"  required/>
        </div>

        <div class="btn">
            <button class="searchBtn">Search</button>
        </div>
    </div>  
   </section>



   <div class="footer">
        <div class="box-container">
            <div class="box">
                <h3>About us</h3>
                <p>Have you Bored being in a Same Place? Want to make ADVENTURE ???</p>
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
   </div>





</body>  
</html>
"""%(rno,rno,rno,rno,rno,rno))