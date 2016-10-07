- References:

https://github.com/pyotp/pyotp

- Timebase
```
daidv@Winner ~/GITHUB/python/standard_library/pytop $ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyotp
>>> pyotp.TOTP('base32secret3232')
<pyotp.totp.TOTP object at 0x7f3a13ee8290>
>>> totp = pyotp.TOTP('base32secret3232')
>>> totp.now()
u'808258'
>>> totp.verify('808258')
True
>>> totp.verify('808258')
True
>>> totp.verify('808258')
True
>>> totp.verify('808258')
True
>>> totp.verify('808258')
False
>>> totp.verify('808258')
False
```

> totp verify series number is False after about 30s

Or we can run time_base.py, the result will be like bello:

```
daidv@Winner ~/GITHUB/python/standard_library/pytop $ python time_base.py
True
False
```
