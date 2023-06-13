from django.shortcuts import render

# Create your views here.
def skills(request):
	acti={"sci":"active"}
	return render(request,"edu/skills.html",acti)