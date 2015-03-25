import matplotlib.pyplot as plt
from numpy import *
from math import *
import pylab
fig,axes=plt.subplots(nrows=1,ncols=2)
data=genfromtxt("q.txt",delimiter="\n")
query=genfromtxt("query.txt",delimiter="\n")
axes[0].plot(data,"g-*")
axes[0].set_title('DATA')
axes[1].plot(query,"b-*")
axes[1].set_title('QUERY')
fig.savefig("querydata.jpg")
