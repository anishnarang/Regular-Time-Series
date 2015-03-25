import matplotlib.pylab as plt 
#from pylab import *
#import matplotlib.pyplot as plt
#import matplotlib.pylab
#print 1
line  = []
with open('Data.txt') as FileObj:
    for lines in FileObj:
	line.append(lines)
#print 2
print "plotting..."
l = line[0]
#print(l[0:400])
l = l.split(' ')
#print('hello')
n = 0

#print(l[0:100])
l = l[1:len(l)-2]
#print(l[0:100])
l1 = []
#print(l[14],l[len(l)-1])
for i in range(0,len(l)):
	if l[i] == '':
		l[i] = 0.0
#		print i
	else:
		l1.append(float(l[i]))

#print(l1[len(l1)-100:len(l1)-1])
	
#print 'type'+str(type(l))

for i in range(0,len(l1)):
	if type(l1[i]) != float:
		print(i)
plt.plot(l1)
plt.show()
