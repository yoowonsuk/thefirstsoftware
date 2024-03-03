class Point:

    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

point1 = Point(10,20)
type(point1)
> __main__.Point

number1 = int("2")
type(number1)
> int 

from geometry import Point
point5 = Point(100,200)
type(point5)
> geometry.Point

import ipaddress
myip = ipaddress.IPv4Address("1.1.1.1")
type(myip)
> ipaddress.IPv4Address

ipaddress.__file__
> '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/ipaddress.py'

print(point5)
> <__main__.Point object at 0x111c7bb70> # repr, str, attribute

'''
if True \
    and True:
'''
