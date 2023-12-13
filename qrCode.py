import qrcode as qr
img=qr.make("Hello") # it create QR code and it returns a PilImage object, in this we provide text or link to generate qr code for that text or link
img.save("message.png") # this will save the qr code in png format in same directory