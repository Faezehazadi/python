import pyqrcode
from pyqrcode import QRCode
test=input("enter your Name and phone number: ")
myQR = QRCode(test)
myQR.show()