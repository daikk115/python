#### How can we print an object that It do not show 

- Create a test.py file with bellow content:

```
class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def __str__(self):
		return "Called str function with: {}" .format(self.arg)

	def __repr__(self):
		return "Called repr function with: {}" .format(self.arg)
```

- From command line this folder which contain test.py file:

```
daidv@Winner /tmp $ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.


>>> from test import *
>>> a = ClassName('Dang Van Dai')
>>> a
Called repr function with: Dang Van Dai
>>> print a
Called str function with: Dang Van Dai
>>> 

```

- What does this mean?

	+ __repr__ function is called when the interactive prompt
	+ __str__ function is called when we use print object

> This is userfull for represent more information for an object, otherwise, we generally see this:

```
>>> from test import *
>>> a = ClassName('Dang Van Dai')
>>> a
<test.ClassName object at 0x7f41bf443810>
>>> print a
<test.ClassName object at 0x7f41bf443810>
>>> 

```

- References:
	+ [how-to-print-a-class-or-objects-of-class-using-print](http://stackoverflow.com/a/1535336/4919442)



