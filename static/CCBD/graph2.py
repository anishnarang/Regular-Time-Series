from matplotlib import *
from numpy import *
from math import *
import pylab
import sys
loc=int(sys.argv[2]) #arg1 is location
m=int(sys.argv[3]) #arg2 is query length
d=str(sys.argv[1]) #arg3 is dataset file
f=open(d,"r")
f1=open("new","w")
i=0
j=0
while(i<loc):
	f.readline()
	i+=1
	j+=1
	if(j==1000000):
		print("."),
		j=0
while(i<(loc+m)):
	s=f.readline()
	f1.write(s)
	i+=1
f.close()
f1.close()
data = genfromtxt("new",delimiter="\n") #change to data file
l=[x for x in range(loc,(loc+m))]
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
pylab.legend(loc="upper right")
pylab.xlabel('Location')
pylab.ylabel('Value')
pylab.savefig("plot.png")

