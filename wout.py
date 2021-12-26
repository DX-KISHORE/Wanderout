#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

print("""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    
    <title>wanderout</title>
    <link rel="stylesheet" href="style1.css">
    
</head>
<body>
    <header class="header">
        <div class="logo">
            <a href="#">Wander Out</a>
            <nav class="navbar">
            <ul class="menu">
                <li><a href="home.py">Home</a></li>
                <li><a href="places.py">Places</a></li>
                <li><a href="package.py">Package</a></li>
                <li><a href="services.py">Service</a></li>
                <li><a href="contact.py">Contact</a></li>
                <li><a href="review.py"><Review</a></li>
                <li><a href="login.py">Login</a></li>
            </ul>
            </nav>
        </div>
    </header>
    
    <div class="content">
        <h3>Adventure is Worthwhile</h3>
        <p>Dicover new places with us, Adventure awaits</p>
    
    <div class="search bar">
        <input type="search" id="serach" name="search placeholder="search here....." required/>
    </div>
    
    <div class="video">
        <video src="images/vid-5.mp4" id="video-slider" loop autoplay muted></video>
    </div>
    </div>

</body>
</html>
""")