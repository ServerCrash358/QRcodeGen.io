# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
 
s = "https://www.pesuacademy.com/Academy/" #input string

url = pyqrcode.create(s) # code to generate the QR code

# Create and save the svg file naming "myqr.svg" (vectors)
url.svg("myqr.svg", scale = 40) 

# Create and save the png file naming "myqr.png" (image)
url.png('F:/myqr.png', scale = 40) 
