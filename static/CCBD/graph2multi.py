from matplotlib import *
from numpy import *
from math import *
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pylab
import sys
loc=int(sys.argv[1]) #arg1 is location
m=int(sys.argv[2]) #arg2 is query length
data = genfromtxt("out",delimiter="\n") #change to data file
l=[x for x in range(loc,(loc+m))]
data=data[loc:(loc+m)]
query = genfromtxt("q.txt",delimiter="\n") #change to query file
query=list(query)
ex=0
ex2=0
for i in range(m):
	ex+=data[i]
	ex2+=(data[i]*data[i])
mean = ex/m
std = ex2/m
std = math.sqrt(std-mean*mean)
for i in range(m):
         data[i] = (data[i] - mean)/std

ex=0
ex2=0
for i in range(m):
	ex+=query[i]
	ex2+=(query[i]*query[i])

mean = ex/m
std = ex2/m
std = math.sqrt(std-mean*mean)
for i in range(m):
         query[i] = (query[i] - mean)/std

pylab.title("Matching region between Candidate and Query")
pylab.grid(True)
pylab.plot(l,data,"-b",label="Candidate")
pylab.plot(l,query,"-g",label="Query")
#blue_patch = mpatches.Patch(color='blue', label='Candidate')
#green_patch = mpatches.Patch(color='green', label='Query')
plt.legend(loc="upper right")
pylab.xlabel('Location')
pylab.ylabel('Value')
pylab.savefig("/home/hduser/django/ccbd/static/plotmulti.png")
