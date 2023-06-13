from django.shortcuts import render

# Create your views here.
def projects(request):
	acti={"proj":"active"}
	return render(request,"pro/project.html",acti)