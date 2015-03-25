from Tkinter import *
import matplotlib.pyplot as plt
from numpy import *
from math import *
import pylab


def show_entry_fields():
	fig,axes=plt.subplots(nrows=1,ncols=1)
	data=genfromtxt("q.txt",delimiter="\n")
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

	plt.show();
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

