from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'app2/index.html')

def team(request):
	return render(request,'app2/team.html')

def tercero(request):
	return render(request,'app2/tercero.html')