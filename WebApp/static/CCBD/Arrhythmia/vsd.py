from matplotlib import *
from numpy import *
from math import *
import pylab
#file1 = input('Enter file')
data = genfromtxt("q.txt",delimiter="  ")
data2 = genfromtxt("Query2.txt",delimiter="  ")
print(len(data))
#print(data)
#for i in data:
#	print i
#f = map(lambda x: 5 * sin(x) , data)
pylab.plot(data2,color="red")
pylab.plot(data, color="black")
pylab.show()
