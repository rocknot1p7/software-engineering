import os
import math
import random
import smtplib

class OTP:
    """
    A class for generating and verifying one-time passwords (OTPs).
    """
    def __init__(self, length, email_address, email_password):
        """
        Initializes an OTP object.
        
        Parameters:
        length (int): The length of the OTP.
        email_address (str): The email address to authenticate with.
        email_password (str): The password for the email address.
        """
        self.length = length
        self.email_address = email_address
        self.email_password = email_password
        
    def generate(self):
        """
        Generates an OTP by picking random digits from the string "0123456789".
        
        Returns:
        str: The generated OTP.
        """
        digits = "0123456789"
        otp = ""
        for i in range(self.length):
            otp += digits[math.floor(random.random() * 10)]
        return otp
    
    def send(self, recipient_email_address, otp):
        """
        Sends the given OTP to the recipient's email address via the Simple Mail Transfer Protocol (SMTP).
        
        Parameters:
        recipient_email_address (str): The email address of the recipient.
        otp (str): The OTP to send.
        
        Returns:
        bool: True if the OTP was successfully sent, False otherwise.
        """
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(self.email_address, self.email_password)
            s.sendmail(self.email_address, recipient_email_address, otp)
            return True
        except Exception as e:
            print(f"Failed to send OTP: {e}")
            return False
        
    def verify(self, sent_otp):
        """
        Verifies if the entered OTP matches the sent OTP.
        
        Parameters:
        sent_otp (str): The OTP that was sent.
        
        Returns:
        bool: True if the entered OTP matches the sent OTP, False otherwise.
        """
        entered_otp = input("Enter Your OTP: ")
        return entered_otp == sent_otp
    
def main():
    email_address = input("Enter your email id: ")
    email_password = ""
    recipient_email_address = input("Enter your email: ")
    otp_length = 10
    otp = OTP(otp_length, email_address, email_password)
    sent_otp = otp.generate()
    if otp.send(recipient_email_address, sent_otp):
        if otp.verify(sent_otp):
            print("Verified")
        else:
            print("Please Check your OTP again")
    else:
         print("Failed to send OTP")

if __name__ == "__main__":
    main()
