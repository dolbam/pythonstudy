# -*- coding: utf-8 -*- 
print "#1"
data = (2, 45, 55, 200, -100, 99, 37, 10284)
for i in data:
	if i%3==0:
		 print(i)
print "\n"
	 
print "#2"
test = "this is test string"
a= test.split()
print a[3], a[2], a[1], a[0]
print "\n"

print "#3"
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print "No. {iteration} is {name}".format(iteration=i, name=name)
print "\n"

print "#4"
# -*- coding: utf-8 -*-
for x in range(2, 10):  
	print("#" + str(x) + "´Ü")
	for y in range(1,10):
		print x,'X',y,'=',x*y
print "\n"

print "#5"
def greet(name):
	print 'hello', name
greet("bob")
greet("john")
print "\n"

print "#6"
temperature = int(input('input temperature\n:'))
if temperature >= 72 :
	print "too hot"
else:
	print "too cold" 
print "\n"

print "#7"
import urllib2
logofile = urllib2.urlopen("http://c1.img.netmarble.kr/web/netmarble/main/v/img/logo.gif")
filename = 'netmarble-logo.gif'
output = open(filename,'wb')
output.write(logofile.read())
output.close()


print "#8"
from datetime import datetime
now = datetime.now()
print 'Today : %s-%s-%s %s:%s' % (now.year, now.month, now.day, now.hour, now.minute)

