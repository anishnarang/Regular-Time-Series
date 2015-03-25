import matplotlib.pyplot as plt
from numpy import *
from math import *
import pylab
fig,axes=plt.subplots(nrows=1,ncols=1)
data=genfromtxt("q.txt",delimiter="\n")
query=genfromtxt("query.txt",delimiter="\n")
x=arange(0,10,0.1)
y1=arange(-1.03598477851339,0.0460997811117354)
y2=arange(-1.03598477851339,-1.04724367512787)

axes.plot(data)
axes.plot(query)
axes.fill_between(0, y1,y2, where=y2>=y1, facecolor="green", interpolate=True)
fig.savefig("querydata_same.jpg")

