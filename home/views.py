from django.shortcuts import render
from home.models import contact,act

# Create your views here.
def home(request):
	acti={"home":"active"}
	return render(request,'home/home.html',acti)

def contact(request):
	acti={"cont":"active"}
	if request.method=="POST":
		sname=request.POST.get('name')
		semail=request.POST.get('email')
		ssub=request.POST.get('sub')
		smsg=request.POST.get('msg')
		reg=act(name32=sname,email32=semail,sub32=ssub,message32=smsg)
		reg.save()
		return render(request,'home/contact.html',acti)
	return render(request,'home/contact.html',acti)

# def savemsg(request):
	
# 	if request.method=="POST":
# 		sname=request.POST.get('name')
# 		semail=request.POST.get('email')
# 		ssub=request.POST.get('sub')
# 		smsg=request.POST.get('msg')
# 		reg=contact(name=sname,email=semail,sub=ssub,message=smsg)
# 		reg.save()
# 		return render(request,'home/contact.html')
