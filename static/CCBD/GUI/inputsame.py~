from Tkinter import *
import matplotlib.pyplot as plt
from numpy import *
from math import *
import pylab


def show_entry_fields():
   #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
	fig,axes=plt.subplots(nrows=1,ncols=2)
	data=genfromtxt(e1.get(),delimiter="\n")
	query=genfromtxt(e2.get(),delimiter="\n")
	axes[0].plot(data,"g-*")
	axes[0].set_title('DATA')
	axes[1].plot(query,"b-*")
	axes[1].set_title('QUERY')
	#fig.savefig("querydata.jpg")  
	plt.show()     
master = Tk()
Label(master, text="Data  FileName").grid(row=0)
Label(master, text="Query FileName").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='CANCEL', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='OK', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )

