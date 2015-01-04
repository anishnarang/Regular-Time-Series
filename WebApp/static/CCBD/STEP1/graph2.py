from matplotlib import *
from numpy import *
from math import *
import pylab
#file1 = input('Enter file')
data = genfromtxt("q.txt",delimiter="\n")
#print(data)
#for i in data:
#	print i
#f = map(lambda x: 5 * sin(x) , data)
data2 = genfromtxt("q2.txt",delimiter="\n")
print(type(data2))
data3 = [0] * 19 # data2
data2 = data3 + list(data2)
pylab.plot(data)
pylab.plot(data2,color="red")
pylab.show()

