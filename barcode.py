import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://github.com/piyushdwivedi8358"
v ="https://www.linkedin.com/in/piyush-dwivedi-1909a5213/"
x ="https://www.instagram.com/piyushdwivedi_12/"
  
# Generate QR code 
url = pyqrcode.create(s)
url =pyqrcode.create(v) 
url =pyqrcode.create(x)
# Create and save the png file naming "myqr.png" 
url.svg("barcodegit.svg", scale = 10 ) 
url.svg("barcodelinkledin.svg",scale=8)
url.svg("insta.svg",scale=9)