""" This program is to create barcodes
"""

import os
import qrcode

img = qrcode.make("https://youtu.be/oHg5SJYRHA0")
img.save("qr.png","PNG")
os.system("open qr.png") 
# to do open is throwing error "'open' is not recognized as an internal or external command,
#operable program or batch file."