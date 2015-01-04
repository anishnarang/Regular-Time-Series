import matplotlib.pyplot as plt
from numpy import *
import sys

f1=open("out","r")
f2=open("new.txt","w")
print("in Fill 1")
loc=int(sys.argv[1])
qlength=int(sys.argv[2])
print("location= :",loc)
i=0
j=0
while(i<=loc):
	f1.readline()
	i+=1
#	print(i)

while(j<=qlength):
	s=f1.readline()
	f2.write(s)
	j+=1
#	print(j)
f1.close()
f2.close()

fig,axes=plt.subplots(nrows=1,ncols=1)
data=genfromtxt("new.txt",delimiter="\n")
query=genfromtxt("query.txt",delimiter="\n")

query1=query
x= arange(0, len(data))
insert(data,1,0)
insert(query,1,0)


l = len(data) - len(query)
print(l)
l1 = array([0]*l)

query = array(list(query) + list(l1))
print(query)
print(data)
print(len(query),len(data))

axes.plot(x,data)
x1=arange(0,len(query1))
axes.plot(x1,query1)

axes.fill_between(x,data,query, where=query<=data, facecolor='yellow', interpolate=True)

plt.savefig("/home/hduser/django/ccbd/static/plot.png")
