#!/usr/bin/env python

'''
Author: Md. Minhazul Haque
Date: 2016-02-05 10:06:59 PM
'''

try:
    from PIL import ImageGrab
except:
    import pyscreenshot as ImageGrab
    
import socket
import StringIO

REFRESH_TIME = 3 # seconds

html_reply = """HTTP/1.0 200 OK
Content-Type: text/html

<html>
<meta http-equiv="refresh" content="{}">
<head>
<title>Desktop</title>
</head>
<body>
<image src="/desktop.png" style="background-size: 100% auto;"
</body>
</html>
""".format(REFRESH_TIME)

image_reply = """HTTP/1.0 200 OK
Content-Type: image/png

"""

# create and start listening for connections
host, port = "0.0.0.0", 8000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
sock.bind((host, port))
sock.listen(10)

print "listening to 8000"

while True:
    csock, (cip, cport) = sock.accept()
    req = csock.recv(1024)
    
    # print client IP
    print "Connection from", cip
    
    if 'GET /desktop.png HTTP/1.1' in req:
        # string buffer to save image
        imbuffer = StringIO.StringIO()
        # get desktop screenshot
        imdesktop = ImageGrab.grab()
        # save image to string buffer
        imdesktop.save(imbuffer, 'png')
        # get image data into variables
        imcontents = imbuffer.getvalue()
        imbuffer.close()
        # write response
        csock.sendall(image_reply + imcontents)

    elif 'GET / HTTP/1.1' in req:
        # send HTML reply
        csock.sendall(html_reply)
    else:
        # send not found error
        csock.sendall("HTTP/1.0 404 Not Found\r\n")
    csock.close()
