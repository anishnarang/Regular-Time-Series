
import matplotlib.pylab as plt
import numpy 
fig,axes = plt.subplots();
axes.set_xlabel('voltage')
axes.set_ylabel('time')
axes.set_title('Voltage versus time')
t= numpy.linspace(0,10,100)
axes.plot(t)
fig.savefig("pic7.jpg")
