import math
import matplotlib.pylab as plt 
l1 = [[1,2,3,4,5],[2,1,4,3,6]]
line = []
with open('arrhythmiadata.txt') as FileObj:
        for lines in FileObj:
                line.append(lines[:len(lines)-1])

l1 = []
for l in line:
        l = l.split(',')
        l1.append(l)
n = 0
l = l1
l1 = []
for i in range(0,len(l)):
        l1.append([])
        for j in range(0,len(l[i])):

		if l[i][j] == '?':
                        l[i][j] = 0.0
                else:
                        l1[i].append(float(l[i][j]))



for i in range(0,len(l1)-1):
	for j in range(1,len(l1)):
		a = l1[i]
		b = l1[j]
		rmsdiff = 0
		for (x, y) in zip(a, b):
    			rmsdiff += (x - y) ** 2  # NOTE: overflow danger if the vectors are long!
		rmsdiff = math.sqrt(rmsdiff / min(len(a), len(b)))
		if i != j:	
			if rmsdiff < 5:
				plt.plot(l1[i],color="red")
				plt.plot(l1[j],color="black")
				plt.show()
				print rmsdiff,"  ",i,"  ",j
				break

