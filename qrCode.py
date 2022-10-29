import pyqrcode
from PIL import Image

link = input("Enter anything to generate QR: ")
qr_code = pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCode.png")

while True:
    query = input("Type something to put in QR: ")
    
    print(query)
    if query == "":
        break

    print("Enter anything to generate QR: \n")