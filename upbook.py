#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb
cgitb.enable()

f = cgi.FieldStorage()
rno = f.getvalue("rno")
print(rno)

conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()

q = """select * from travel where idno='%s'"""%(rno)
cur.execute(q)

r = cur.fetchall()

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
    <link rel="stylesheet" href="s5.css"
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
<div class="full-page">

   <h1 class="heading">BOOKING STATUS</h1>
   <center>
    <table class="table">
    <thead>
    <tr>
        <th>id</th> 
        <th>Traveler Id</th> 
        <th>Full name</th>
        <th>Age</th>
        <th>Gender</th>
        <th>Phone number</th>
        <th>Booked Places</th>
        <th>Form Date</th>
        <th>To Date</th>
        <th>Address</th>
        <th>City</th>
        <th>State</th>
        <th>Pincode</th>
        <th>Edit Details</th>
        <th>Cancel Ticket</th>
    </tr>
    </thead>
    <div>
""")
count = 0
for i in r:
    count = count + 1
    print("""
    <tbody>
    <tr class="row">
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td><a class="btn" href="edit_booking.py?id=%s">Edit</a></td>
        <td><a class="btn" href="delete_booking.py?id=%s">Cancel</a></td>
    </tr>
    </tbody>
    """ %(count, i[1], i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[0],i[0]))

print("""

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

</table>
</center>
</body>
</html>
""")