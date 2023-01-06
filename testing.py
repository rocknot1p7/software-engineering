import os
import math
import random
import smtplib
# testing
import unittest
import re

def email_check(mail): 

    compil = re.compile(r"""^([-a-z0-9_]+((\w)+[-a-z0-9_]+(\w)+)?)@[-a-z0-9_]+[.]([-a-z0-9_]+([.][-a-z0-9_]+)?)$""", re.X)
    result = compil.search(mail)
    if result:
        length = mail.split('@')
        if len(length[0]) <= 128 and len(length[1]) <= 256:
            print( mail, 'correct' if not '-.' in length[1] and not '.-' in length[1] else 'Incorrect value')
            return result.group()
        else:
            print ('Length string is not mathing')
    else:
        print ('Incorrect data')
    return ""
    

class TestingEmail(unittest.TestCase):
    def setUp(self):
        self.mails=["prathamehsogale@gmail.com","sdfa@gmail.com","pratham@dbatu.ac.in"]
        print("hello")
    def test_EmailCheck(self):
        for i in self.mails:
            self.assertTrue(i==email_check(i),"INCORRECT Value")
    def tearDown(self):
        self.mails=[""]
#def digit():
#    i=int(input("Enter the lenght of otp you want"))
#    return i
def getOtp(value):
    digits="0123456789"
    for i in range(d):
        Otp+=digits[math.floor(random.random()*10)]
    return Otp;
    
def login_id():
    i=input("Enter your email id")
    return i
#OTP=""
#d=digit()
#for i in range(d):
#    OTP+=digits[math.floor(random.random()*10)]
#otp = OTP + " is your OTP"
#msg= otp
#print(otp)
if __name__=='__main__':
    unittest.main()
 
    
