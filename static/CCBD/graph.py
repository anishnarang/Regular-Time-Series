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
pylab.plot(data)
pylab.show()

