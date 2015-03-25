import matplotlib.pyplot as plt
from numpy import *
'''m = array()
n = array()
fp1 = open("query.txt","r")
if(fp1):
	lines = map(str.strip,fp1.readlines())
fp1.close()
for line in lines:
	m = m + line.split()
#print(m)
m = map(float, m)
#y1 = arange(m[0], m[len(m)-1])

fp2 = open("q.txt","r")
if(fp2):
        lines = map(str.strip,fp2.readlines())
fp2.close()
for line in lines:
        n = n + line.split()
n = map(float, n)

y2 = arange(n[0], n[len(n)-1])

l=len(m)-len(n)
m += [0]*l

y1 = arange(m[0], m[len(m)-1])

x = arange(0.0,140,0.01)
print(len(y1),len(y2))
print(m)
print(n)
#print(y1)
#print(y2)
'''

#x = arange(0,128)
#print(len(x))
fig,axes=plt.subplots(nrows=1,ncols=1)
data=genfromtxt("q.txt",delimiter="\n")
query=genfromtxt("query.txt",delimiter="\n")

query1=query
x= arange(0, len(data))
insert(data,1,0)
insert(query,1,0)

#axes.plot(x,data)
#axes.plot(x,query)
#axes.plot(query)
l = len(data) - len(query)
print(l)
#print(len(data))
#print(len(query))
l1 = array([0]*l)
'''print(l1)
print(type(l1))
concatenate((query, l1))
print(len(data))
print(query)'''
query = array(list(query) + list(l1))
print(query)
print(data)
print(len(query),len(data))
data1 = array(list(data)[0:len(query1)])
x1 = arange(0,len(query1))
axes.plot(x1,data1)
axes.plot(x,query)
'''for i in range(len(m)):
	y1 = n[i]
	y2 = m[i]'''
axes.fill_between(x,data,query,where=query>=data,facecolor='green', interpolate=True)

plt.show();
