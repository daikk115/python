import pyotp
import time

totp = pyotp.TOTP('base32secret3232')
series = totp.now()

# OTP verified for current time
print totp.verify(series) # => True
time.sleep(30)
print totp.verify(series) # => False
