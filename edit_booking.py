#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb
cgitb.enable()

f = cgi.FieldStorage()
id = f.getvalue("id")
print(id)

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
                    <li><a href='home.py'>Home</a></li>
                    <li><a href='places.py'>Places</a></li>
                    <li><a href='b_login.py'>Booking Status</a></li>
                     <li><a href='review.py'>Reviews</a></li>
                    <li><a href='contact.py'>Contact</a></li>
                    <li><button class='loginbtn' onclick="location.href='home.py';">Logout</button></li>
                </ul>
            </nav>
        </div>

      <div class="full-page">
      <div class="center">
      <h1>Edit Tickect</h1>
        <form >
        <div class="text">
        <h3>S.no:</h3>
                <input type="text" id="idno" name="idno" value=%s readonly required/>
        </div>
        <div class="text">
        <h3>Full name:</h3>
                <input type="text" id="fname" name="fname" required/>
        </div>

        <div class="text">
         <h3>Age:</h3>
                <input type="number" id="age" name="age" min="1" max="100"  required/>
                </div>
            <div class="text">
             <h3>Gender:</h3>
                <h3 class="h3"><input type="radio" id="gender" name="gender" value="Male">Male<input type="radio" name="gender" id="gender" value="Female">Female</h3>
                </div>


            <div class="text">
             <h3>Phone number:</h3>
                <input type="tel" id="phno" name="phno" placeholder="0123-45-6789" pattern="[0-9]{4}-[0-9]{2}-[0-9]{4}" required/>
                </div>
            <div class="text">
             <h3>Where to go:</h3>
                <input type="text" id="location" name="location" placeholder="Places"  required/>
                </div>

            <div class="text">
             <h3>From date:</h3>

                <input type="date" id="fdate" name="fdate" required/>
                </div>
            <div class="text">
             <h3>To date:</h3>

                <input type="date" id="tdate" name="tdate"  required/>
                </div>
            <div class="text">
             <h3>Number of person:</h3> 
                <input type="number" id="person" name="person"  min="1" max="100" required/>
                </div>
            <div class="text">
             <h3>Address:</h3>
                <input type="message" id="address" name="address"  required/>
                </div>
            <div class="text">
             <h3>City:</h3>
                <select class="option" name="city" id="city">
            <option default>Madurai</option>
            <option default>Chennai</option>
            <option default>Coimbatore</option>
            <option default>Other</option>
        </select>
        </div>
         <div class="text">
          <h3>State:</h3>
          <select class="option" name="state" id="state">
            <option default>Tamilnadu</option>
           <option default>Kerala</option>
           <option default>Maharashtra</option>
           <option default>Other</option>
        </select>
        </div>
        <div class="text">
        <h3>Pincode</h3>
        <input type="number" id="pin" name="pin" class="pin"  min="1000" max="1000000" required/>
        </div>

        <input type="submit" class="submit" id="sub" name="sub" value="Save">

      </form>
    </div>
    </div>

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
"""%(id))

sub = f.getvalue("sub")
# print(f)

if sub != None:
    id = f.getvalue("idno")
    fname = f.getvalue("fname")
    age = f.getvalue("age")
    gender = f.getvalue("gender")
    phno = f.getvalue("phno")
    location = f.getvalue("location")
    fdate = f.getvalue("fdate")
    tdate = f.getvalue("tdate")
    person = f.getvalue("person")
    address = f.getvalue("address")
    city = f.getvalue("city")
    state = f.getvalue("state")
    pin = f.getvalue("pin")

    conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
    cur = conn.cursor()

    q = """UPDATE travel SET id='%s',fullname='%s',age='%s',gender='%s', phonenumber='%s',location='%s', fromdate='%s', todate='%s', 
    person='%s' ,address='%s', city='%s',state='%s', pincode='%s' where id='%s'"""\
        %(id,fname, age, gender, phno, location, fdate, tdate, person, address, city, state, pin,id)

    cur.execute(q)
    conn.commit()
    print("""
        <script>
        alert("Edited successfully");
        location.href='b_login.py';
        </script>
        """)
    conn.close()
