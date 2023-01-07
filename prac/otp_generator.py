import os
import math
import random
import smtplib
#def digit():
#    i=int(input("Enter the lenght of otp you want"))
#    return i
def generate_otp(value):
    digits="0123456789"
    otp=int(0)
    for i in range(value):
        otp=otp*10+int(digits[math.floor(random.random()*10)])
    return otp;
    
def login_id():
    i=input("Enter your email id")
    return i
#OTP=""
#d=digit()
#for i in range(d):
#    OTP+=digits[math.floor(random.random()*10)]
#otp = OTP + " is your OTP"
#msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
email_identity=login_id()
msg=str(generate_otp(10))
s.login(email_identity, "")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == msg:
    print("Verified")
else:
    print("Please Check your OTP again")
