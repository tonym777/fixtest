"""
Created on Fri June 6th 22:59:04 2025

Simple Operator for 2FA by using Timebase OneTime Password method
@author: Tony
"""

import pyotp
from pyotp import TOTP

import qrcode



class MFAOperator:

    def __init__(self):
        self.issue_name="MyApp"
        self.secret_key=pyotp.random_base32()
        self.totp = TOTP(self.secret_key)


    def generate_onetime_otp_code(self) -> str:
        return self.totp.now()


    def verify_opt(self, otp_code) -> bool:
        return self.totp.verify(otp_code)


    def generate_otp_url(self, user) -> str:
        return self.totp.provisioning_uri(user, self.issue_name)


    def generate_qr_code(self, user, image_file):
        otp_url = self.generate_otp_url(user)
        qrcode.make(otp_url).save(image_file)
