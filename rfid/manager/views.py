from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from manager.models import StudentData, Mess


def index(request):
	context={}
	return render(request, 'manager/index1.html', context)

def enter(request):
	students=StudentData.objects.all()
	context={'students':students}
	return render(request, 'manager/enter.html', context)

def detail(request, rollnumber):
	student= get_object_or_404(StudentData, roll_number=rollnumber)
	cols=list(student._meta.get_all_field_names())
	# indices=[0,2,4,5,7,8,9,10,12,13,15,17,20,21]
	indices=[1,3,6,11,14,16,18,19]

	cols1=[]
	for i in indices:
		cols1.append(cols[i])
	values=[]
	for col in cols1:
		values.append(getattr(student, col))
	aa=0
	d=""
	strk=0
	guest=0
	row=Mess.objects.filter(roll_number=rollnumber).count()
	if row==0:
		a=0
	else:
		a=Mess.objects.get(roll_number=rollnumber)
		aa=a.attendance
		d = a.date
		strk = a.streak
		guest = a.guest



	# try:
	# 	row=Mess.objects.get(roll_number=rollnumber)
 #    except Mess.DoesNotExist:
 #    						raise Http404
        # raise Http404
	comb= zip(cols1, values)
	dues = aa * 25
	totdues = dues + (guest * 50)
	context={'student':student, 'dues': dues, 'cols':cols,'attendance':aa, 'totdues':totdues, 'comb':comb, 'streak' :strk, 'lmeal' :d, 'guest':guest }
	return render(request, 'manager/detail1.html', context)

def entered(request):
	roll=request.POST['rollno']
	# student= get_object_or_404(StudentData, roll_number=roll)
	return HttpResponseRedirect(reverse('detail', args=(roll,)))

def allstudents(request):
	students=StudentData.objects.all()
	context={'students':students}
	return render(request, 'manager/allstudents.html', context)
