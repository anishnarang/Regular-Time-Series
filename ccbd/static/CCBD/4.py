import matplotlib.pyplot as plt
import numpy as np
n=np.array(range(5))
fig,axes = plt.subplots(nrows =1 ,ncols = 1)
axes.set_xlabel('sales')
axes.set_ylabel('expenditure')
axes.set_title('Bar graph for CompanyA')
axes.bar(n,n**2,align="center", width=0.5, alpha=0.5)
fig.savefig("pic4.jpg");
