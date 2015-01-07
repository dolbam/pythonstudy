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
    