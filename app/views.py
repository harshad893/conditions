from django.shortcuts import render

# Create your views here.
def hai(request):
    d={'a':1900,'b':15,'c':1000}    
    return render(request,'hai.html',d)