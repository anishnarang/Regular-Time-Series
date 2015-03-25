from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib import messages
import os,time
from .forms import *
from webapp.models import *

def timer():
	f=open("file.txt","r")
	usr=""
	sys=""
	l=0
	for line in f:
		line=line.split(" ")
		if("elapsed" in line[2]):
			for char in line[2]:
				if(char=="e"):
					break
				else:
					usr=usr+char
	f.close()
	f=open("loc.txt","r")
	line=f.read().strip(" ").split("\n")
	print(line)
	l=int(line[1])
	d=float(line[2])
	t=usr
	return (t,l,d)

# Create your views here.
t=0
tm=0
l1,l2,d1,d2=0,0,0,0
def input(request):
	global t
	global tm,l1,l2,d1,d2
	form=DetailsForm(request.POST or None)
	if form.is_valid():
		save_it=form.save(commit=False)
		save_it.save()
		q=InputForm.objects.all()[InputForm.objects.count()-1]
        	qsize=q.EnterQuerySize
        	points=q.EnterPoints
		print(points)		## Size of file selected
		print(qsize)		##Query size to be generated
## Run script.sh
		home=os.getenv("HOME")
		os.chdir(home+"/cloaked-octo-lana/static")
		mkstr="./script.sh %d" % (int(qsize)//2)
		os.system(mkstr)
## Running UCR
		os.chdir(home)
		os.chdir(home+"/cloaked-octo-lana/static/trillion/SourceCode")
		mkstr="time --output=file.txt ./a.out %s q.txt 128 0.05 > loc.txt" % str("~/ccbd_data/"+points)
		#mkstr="time --output=file.txt ./a.out %s q.txt 128 0.05 > loc.txt" % str(points)
		#mkstr="time --output=file.txt ./a.out out q.txt 128 0.05 > loc.txt"
		print(mkstr)
		print("In UCR")
		os.popen(mkstr)
		t,l1,d1=timer()
		print("UCR Real time :",t)
## multicore code
		os.chdir(home)
		os.chdir(home+"/cloaked-octo-lana/static/multicore")
		print("In multicore")
		mkstr="time --output=file.txt ./a.out %s q.txt 128 0.05 > loc.txt" % str("~/ccbd_data/"+points)
		#mkstr="time --output=file.txt ./a.out %s q.txt 128 0.05 > loc.txt" % str(points)
		#mkstr="time --output=file.txt ./a.out out Query.txt 128 0.05 > loc.txt"
		os.popen(mkstr)
		tm,l2,d2=timer()		
		print("Multicore real time : ",tm) 
## Plotting
		mkstr="python graph2.py %s %d %d" % ("~/ccbd_data/"+points,l1,qsize)
		os.chdir(home)
		os.chdir(home+"/cloaked-octo-lana/static/CCBD/")
		print("Plotting")
		os.system(mkstr)
		return render_to_response("images.html",{"time":t,"timemulti":tm,"distance":d1,"distancemulti":d2,"location":l1,"locationmulti":l2},context_instance=RequestContext(request))
	
	return render_to_response("input.html",locals(),context_instance=RequestContext(request))


def images(request):
	return render_to_response("images.html",{"time":t,"timemulti":tm},context_instance=RequestContext(request))

def TimeSeries(request):
	return render_to_response("TimeSeries.html",locals(),context_instance=RequestContext(request))

def Mahalanobis(request):
	form=MahaForm(request.POST or None)
	if form.is_valid():
        	save_it=form.save(commit=False)
        	save_it.save()
        	q=InputMaha.objects.all()[InputMaha.objects.count()-1]
        	qsize=q.EnterQuerySize
		home=os.getenv("HOME")
	
		os.chdir(home)
		os.chdir(home+"/cloaked-octo-lana/static/IrregularTS/")
		print("Size: ",qsize)
		mkstr="python irregen.py %s" % (str(qsize))
		os.popen(mkstr)
		print "Running Maha"
		return render_to_response("maha_images.html",locals(),context_instance=RequestContext(request))	
	return render_to_response("inputmaha.html",locals(),context_instance=RequestContext(request))

