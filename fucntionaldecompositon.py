import os
import math
import random
import smtplib

def generate_otp(length):
    """
    Generates a one-time password (OTP) of a given length by picking random digits from the string "0123456789".
    
    Parameters:
    length (int): The length of the OTP.
    
    Returns:
    str: The generated OTP.
    """
    digits = "0123456789"
    otp = ""
    for i in range(length):
        otp += digits[math.floor(random.random() * 10)]
    return otp

def login_id():
    """
    Asks the user for their email address.
    
    Returns:
    str: The user's email address.
    """
    return input("Enter your email id: ")

def send_otp(otp, email_address, email_password, recipient_email_address):
    """
    Sends the given OTP to the recipient's email address via the Simple Mail Transfer Protocol (SMTP).
    
    Parameters:
    otp (str): The OTP to send.
    email_address (str): The email address to authenticate with.
    email_password (str): The password for the email address.
    recipient_email_address (str): The email address of the recipient.
    
    Returns:
    bool: True if the OTP was successfully sent, False otherwise.
    """
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(email_address, email_password)
        s.sendmail(email_address, recipient_email_address, otp)
        return True
    except Exception as e:
        print(f"Failed to send OTP: {e}")
        return False

def verify_otp(sent_otp):
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
    email_address = login_id()
    email_password = "jkzi tlir xiiu apts"
    recipient_email_address = input("Enter your email: ")
    otp_length = 10
    sent_otp = generate_otp(otp_length)
    if send_otp(sent_otp, email_address, email_password, recipient_email_address):
        if verify_otp(sent_otp):
            print("Verified")
        else:
            print("Please Check your OTP again")
    else:
        print("Failed to send OTP")

if __name__ == "__main__":
    main()
