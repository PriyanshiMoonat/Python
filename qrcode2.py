# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 21:58:42 2024

@author: priyanshi
"""

import qrcode as qr
from PIL import Image
qr=qr.QRCode(version=1,error_correction=qr.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://www.python.org/")
qr.make(fit=True)
img=qr.make_image(fill_color="teal")
img.save("linkedinqrcode.png")