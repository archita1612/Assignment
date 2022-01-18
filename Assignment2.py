print("Welcome to ABC Hotel")
phone_number = input("Enter your phone number:\n")
print(f"An OTP has been sent to {phone_number}")

import random
import pyqrcode
import png
from pyqrcode import QRCode
otp = (str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)))
print(otp)
print("Scan the QR code to view the menue")
#Data to be imported
data=("""Uttapam, Biryani, Rice, Thali, Dosa, Idli""")
#Encoding data in QR code
url = pyqrcode.create(data)
# Saving image file
url.svg("myqr.svg", scale = 8)
url.png("myqr.png", scale = 6)
customer_otp = (input("Enter your OTP:\n"))
if otp == customer_otp:
   

    Uttapam_price = 200
    Biryani_price = 150
    Rice_price = 50
    Thali_price = 180
    Dosa_price = 80
    Idli_price = 65

    order = input("Enter the item you wanna order:\n").lower
    if (order=="Uttapam"):
        qty = int(input("Enter the quantity you wanna order\n"))
        print(f"Your bill is {Uttapam_price * qty} + {(Uttapam_price * qty ) * 10/100}")
    elif order =="Biryani":
        qty = int(input("Enter the quantity you wanna order\n"))
        print(f"Your bill is {Biryani_price * qty} + {(Biryani_price * qty ) * 10/100}")
    elif order =="Rice":
        qty = int(input("Enter the quantity you wanna order\n"))
        print(f"Your bill is {Rice_price * qty} + {(Rice_price * qty ) * 10/100}")
    elif order =="thali":
        qty = int(input("Enter the quantity you wanna order\n"))
        print(f"Your bill is {Thali_price * qty} + {(Thali_price * qty ) * 10/100}")
    elif order =="Dosa":
        qty = int(input("Enter the quantity you wanna order\n"))
        print(f"Your bill is {Dosa_price * qty} + {(Dosa_price * qty ) * 10/100}")
    elif order =="Idli":
        qty = int(input("Enter the quantity you wanna order\n"))
        print(f"Your bill is {Idli_price * qty} + {(Idli_price * qty ) * 10/100}")
    else:
        print("We don't serve this item")    

else:
    print("Opps! you've entered the wrong OTP.")
