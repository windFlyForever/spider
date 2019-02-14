#coding=utf-8

import os
from person import Person

a = 3.222222

print "输入数值：%.2f" %(a)

print "saa{a}xx{b}".format(a="dog", b="cat")

print os.getcwd()

print os.path.isdir("tieba/")

print os.path.isfile("urlspider.py")

print os.listdir("/Users/windfly/PycharmProjects/spider")

print os.stat("urlspider.py")

try:
    p = Person('a', 13)
    print p.age, p.name
    print str(p)
except Exception, args:

    print args

