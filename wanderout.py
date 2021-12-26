#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb, os, smtplib
cgitb.enable()

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css" />

    <title>WANDEROUT</title>
    <link rel="stylesheet" href="style.css">

</head>
<body>
    <div class="full-page">
        <div class="navbar">
            <div>
                <a href='website.html'>WANDEROUT</a>
            </div>
            <nav>
                <ul id='MenuItems'>
                    <li><a href='#'>Home</a></li>
                    <li><a href='#'>Places</a></li>
                    <li><a href='#'>Package</a></li>
                    <li><a href='#'>Reviews</a></li>
                    <li><a href='#'>Services</a></li>
                    <li><a href='#'>Contact</a></li>
                    <li><button class='loginbtn' onclick="location.href='home.py';">Login</button></li>
                </ul>
            </nav>
        </div>
    </div>
    <div class="background">
    <section>
    <div class="content">
        <h3>Adventure is Worthwhile</h3>
        <p>Dicover new places with us, Adventure awaits</p>    
        <div class="search">
            <input type="text" name="search" class="query" required/>
        </div>
    
        <div class="btn">
            <button class="searchbtn">Search</button>
        </div>
    </div>
    
   
       
       
        <div id='login-form' class='login-page'>
            <div class="form-box">
                <div class='button-box'>
                    <div id='btn'></div>
                    <button type='button' onclick='login()' class='toggle-btn'>Log In</button>
                    <button type='button' onclick='register()' class='toggle-btn'>Register</button>
                </div>
                <form id='login' class='login'>
                    <input type='text' name="email1" class='textbox' placeholder='Email Id' required />
                    <input type='password' name="pwd1" class='textbox' placeholder='Enter Password' required />
                    <input type='checkbox' class='checkbox'> <span>Remember Password</span>
                    <button type='submit' name="sub1" class='submitbtn'>Log in</button>
                </form>

                <form id='register' class='register'>
                    <input type='text' name="fname" class='textbox' placeholder='First Name' required />
                    <input type='text' name="lname" class='textbox' placeholder='Last Name' required />
                    <input type='email' name="email" class='textbox' placeholder='Email Id' required />
                    <input type='password' name="pwd" class='textbox' placeholder='Enter Password' required />
                    <input type='password' name="cpwd" class='textbox' placeholder='Confirm Password'  required />
                    <input type='checkbox' class='checkbox'><span>I agree to the terms and conditions required /</span>
                    <button type='submit' name="sub" class='submitbtn'>Register</button>
                </form>
            </div>
        </div>
    </div>
         <script>
        var x=document.getElementById('login');
        var y=document.getElementById('register');
        var z=document.getElementById('btn');
        function register()
        {
        x.style.left='-400px';
        y.style.left='50px';
        z.style.left='110px';
        }
        function login()
        {
        x.style.left='50px';
        y.style.left='450px';
        z.style.left='0px';
        }
    </script>
    <script>
        var modal = document.getElementById('login-form');
        window.onclick = function(event) 
        {
            if (event.target == modal) 
            {
                modal.style.display = "none";
            }
        }
    </script>
     </section> 
    
    <!-- footer section  -->

    <section class="footer">

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
            <a href="package.py">Package</a>
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


</section>


    
</body>
</html>
""")

conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()

f = cgi.FieldStorage()
sub = f.getvalue("sub")
fname = f.getvalue("fname")
lname = f.getvalue("lname")
email = f.getvalue("email")
pwd = f.getvalue("pwd")
cpwd = f.getvalue("cpwd")

#print(f)

if sub != None:
    q = """INSERT INTO reg(First,Last,Email,Password,Confirm) values('%s','%s','%s','%s','%s')""" %(fname,lname,email,pwd,cpwd)
    cur.execute(q)
    conn.commit()
    print("""
        <script>
        alert("Account created successfully");
        </script>
        """)
    conn.close()


