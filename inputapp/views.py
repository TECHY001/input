from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def result(request):
    mobile=int(request.GET['mobile'])
    keyboard=int(request.GET['keyboard'])
    monitor=int(request.GET['monitor'])
    total=mobile+keyboard+monitor
    


    return render(request,'request.html',{'result':total})