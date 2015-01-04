from random import randrange
import datetime,pandas
import numpy as np
from matplotlib import *
from math import *
import pylab,sys,os

m=int(sys.argv[1])	## Number of points of candidate
q=int(sys.argv[2])	## Number of points of query
n=int(sys.argv[3])	## Number of points to be made None
d1=dict()
d2=dict()

valuel = list(np.random.randn(m))
queryl = list(np.random.randn(q))

for i in range(len(valuel)):
	d1[i+1]=valuel[i]
for i in range(len(queryl)):
	d2[i+1]=queryl[i]
for i in range(n):
	r=randrange(1,m+1)
	d1[r]=None

finalval=[]
finalquery=[]

for i in range(1,m+1):
	finalval.append(d1[i])
for i in range(1,q+1):
	finalquery.append(d2[i])

os.remove("Data.txt")
os.remove("Query.txt")
f1=open("Data.txt","w")
f2=open("Query.txt","w")

for i in finalval:
	f1.write(str(i)+"\n")
for i in finalquery:
	f2.write(str(i)+"\n")
f1.close()
f2.close()

def MahalanobisDist(x, y):
    covariance_xy = np.cov(x,y, rowvar=0)
    inv_covariance_xy = np.linalg.inv(covariance_xy)
    xy_mean = np.mean(x),np.mean(y)
    x_diff = np.array([x_i - xy_mean[0] for x_i in x])
    y_diff = np.array([y_i - xy_mean[1] for y_i in y])
    diff_xy = np.transpose([x_diff, y_diff])
    
    md = []
    for i in range(len(diff_xy)):
        md.append(np.sqrt(np.dot(np.dot(np.transpose(diff_xy[i]),inv_covariance_xy),diff_xy[i])))
    return sum(md)


count=0
loc=0
mahaldist=100000000
for i in range(len(finalval)-len(finalquery)+1):
	x=finalval[i:(i+q)]
	prev=0
	j=0
	md=0
	count=0
#	print(x)
	for k in x:
		if(k != None):
			count+=1
#	print("count :", count)
	while(j<len(x)):
		if(x[j]==None):
			y=x[prev:(j)]
			query=finalquery[prev:(j)]
			j+=1
			prev=j
			if(len(y)>0):
				md+=MahalanobisDist(y,query)
		else:
		
			j+=1
	y=x[prev:j]
	query=finalquery[prev:j]
	if(len(y)>0):
		md+=MahalanobisDist(y,query)
	ml=md/count
	if(mahaldist>ml):
                mahaldist=ml
                loc=i
	print(mahaldist,ml,i)
	
print("Location:",loc)
print("Distance:",mahaldist)
pylab.plot([x for x in range((loc),(loc+q))],finalval[(loc):(loc+q)],"-b",label="candidate")	
pylab.plot([x for x in range(loc,(loc+q))],finalquery,"-g",label="query")
pylab.legend(loc="upper right")
pylab.savefig("plot.png")
#md=MahalanobisDist(finalval,finalquery)
#print(md)


