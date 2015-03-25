import matplotlib.pyplot as plt
from numpy import *
from math import *
import pylab
fig,axes=plt.subplots(nrows=1,ncols=1)
data=genfromtxt("q.txt",delimiter="\n")
query=genfromtxt("query.txt",delimiter="\n")
axes.plot(data)
axes.plot(query)
fig.savefig("querydata_same.jpg")

