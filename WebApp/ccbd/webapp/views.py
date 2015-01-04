from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib import messages
import os,time
from .forms import DetailsForm
from webapp.models import InputForm
# Create your views here.
t=0
tm=0
def input(request):
	global t
	global tm
	form=DetailsForm(request.POST or None)
	if form.is_valid():
		save_it=form.save(commit=False)
		save_it.save()
		q=InputForm.objects.all()[InputForm.objects.count()-1]
        	qsize=q.EnterQuerySize
        	points=q.EnterPoints
		print(points)
        	print(qsize)
        	home=os.getenv("HOME")
        	os.chdir(home+"/django/ccbd/static")
        	#mdstr="./script.sh %d" % (points//2)
		#os.system(mdstr)
		
		os.chdir(home)
		os.chdir(home+"/django/ccbd/static/trillion/SourceCode")
		t1=time.clock()
		l=(os.popen("time --output=file.txt ./a.out out Query.txt 128 0.05 > loc.txt").read())
		t2=time.clock()
		t=(t2-t1)*1000
		print("Python Time taken= ",t)
	

		f=open("file.txt","r")
		usr=""
		sys=""
		for line in f:
			line=line.split(" ")
			if("user" in line[0] and "system" in line[1]):
				for char in line[0]:
					if(char=="u"):
						break
					else:
						usr=usr+char
				for char in line[1]:
					if(char=="s"):
						break
					else:
						sys=sys+char
		f.close()
		f=open("loc.txt","r")
		for line in f:
			line=line.split("\n")
			loc=line
		l=int(loc[0])
		print(float(usr))
		print(float(sys))
		t=float(usr)+float(sys)
		print("Total CPU time :",t)

		mdstr1="python graph2.py %d %d" % (l,qsize)
		os.chdir(home)
		os.chdir(home+"/django/ccbd/static/CCBD/")
		print("In directory")
		os.system(mdstr1)


## multicore code
		os.chdir(home)
                os.chdir(home+"/django/ccbd/static/multicore")
		print("In multicore")
                t3=time.clock()
                l=(os.popen("time --output=file.txt ./a.out out Query.txt 128 0.05 > loc.txt").read())
		t4=time.clock()
		tm=(t4-t3)*1000
		print("Python multicore Time taken= ",tm)
		

		f=open("file.txt","r")
		usr=""
		sys=""
		for line in f:
			line=line.split(" ")
			if("user" in line[0] and "system" in line[1]):
				for char in line[0]:
					if(char=="u"):
						break
					else:
						usr=usr+char
				for char in line[1]:
					if(char=="s"):
						break
					else:
						sys=sys+char
		f.close()
		f=open("loc.txt","r")
		for line in f:
			line=line.split("\n")
			loc=line
		l=loc
		tm=float(usr)+float(sys)
		print("Total multicore CPU time :",tm)


		return render_to_response("images.html",{"time":t,"timemulti":tm},context_instance=RequestContext(request))

	return render_to_response("input.html",locals(),context_instance=RequestContext(request))

def images(request):
	return render_to_response("images.html",{"time":t,"timemulti":tm},context_instance=RequestContext(request))

def TimeSeries(request):
	return render_to_response("TimeSeries.html",locals(),context_instance=RequestContext(request))
	
