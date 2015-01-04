import matplotlib.pyplot  as plt
import numpy as np
x=np.arange(10)
y=x+(x*2)
fig,axes=plt.subplots(nrows=1, ncols=2)
for ax in axes:
	ax.plot(x,y,'g-*')
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_title('title')
fig.savefig("sample.jpg")
