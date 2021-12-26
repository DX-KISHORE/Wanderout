#!C:/Users/kishore/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import cgi, pymysql, cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost", user="root", password="", database="julybatch")
cur = conn.cursor()

q = """select * from personaldata """
cur.execute(q)

r = cur.fetchall()

print("""
<html>
<body>
<i><center><h1>PERSONAL INFORMATION</h1></center><i>

<center>
    <h2><i>person Details</i></h2>
    <table cellspacing="0" cellpadding="15" border="5">
    <tr>
        <th>Sno</th> 
        <th>Name</th> 
        <th>Gender</th> 
        <th>DOB</th> 
        <th>Age</th> 
        <th>Phone.no</th>
        <th>District</th>
        <th>State</th> 
        <th>Email id</th> 
    </tr>
""")
count = 0
for i in r:
    count = count + 1
    print("""
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
    """ % (count, i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))

print("""
</table>
</center>
</body>
</html>
""")