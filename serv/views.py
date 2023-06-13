from django.shortcuts import render

# Create your views here.
def services(request):
	acti={"ser":"active"}
	return render(request,"serv/service.html",acti)