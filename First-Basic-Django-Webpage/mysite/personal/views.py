from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request,'personal/basic.html',{'content': ['If you would like to contact me, pls email me','Sahejeetsingh97@gmail.com']})
