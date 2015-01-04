import matplotlib.pylab as plt 
#from pylab import *
#import matplotlib.pyplot as plt
#import matplotlib.pylab
line  = []
with open('arrhythmiadata.txt') as FileObj:
	for lines in FileObj:
		line.append(lines[:len(lines)-1])

l1 = []
for l in line:
#	print(l[0:400])
	l = l.split(',')
#	print l
	l1.append(l)
#	break;
n = 0
l = l1
l1 = []
for i in range(0,len(l)):
#	print(l[i])
	l1.append([])
	for j in range(0,len(l[i])):
	
		if l[i][j] == '?':
			l[i][j] = 0.0
		else:
			l1[i].append(float(l[i][j]))

	
'''
for i in range(0,len(l1)):
	if type(l1[i]) != float:
		print(i)
'''

print("Plotting each arrhythmia data set one by one")
cnt = 0;
for i in l1:
	plt.plot(i)
	plt.show()
	if cnt > 5:
		break
	cnt += 1

