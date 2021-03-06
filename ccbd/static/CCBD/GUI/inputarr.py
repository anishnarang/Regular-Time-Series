from Tkinter import *
import matplotlib.pyplot as plt
from numpy import *
from math import *
import pylab


def show_entry_fields():
   	
	line  = []
	with open(e1.get()) as FileObj:
		for lines in FileObj:
			line.append(lines[:len(lines)-1])

	l1 = []
	for l in line:
		l = l.split(',')
	l1.append(l)
	n = 0
	l = l1
	l1 = []
	for i in range(0,len(l)):
#	print(l[i])
		l1.append([])
		for j in range(0,len(l[i])):
			if l[i][j] == '?':
				l[i][j] = 0.0
			else:
				l1[i].append(float(l[i][j]))

	

	print("Plotting each arrhythmia data set one by one")
	cnt = 0;	
	for i in l1:
		plt.plot(i)
		plt.show()
		if cnt > 5:
			break
		cnt += 1

master = Tk()
Label(master, text="Arrhythmia Data FileName").grid(row=0)
#Label(master, text="Query FileName").grid(row=1)

e1 = Entry(master)
#e2 = Entry(master)

e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)

Button(master, text='CANCEL', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='OK', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )

