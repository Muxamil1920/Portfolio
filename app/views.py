from django.shortcuts import render
from . models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        
        contact=Contact(name=name ,email=email,number=number,subject=subject,message=message)
        contact.save()
        
    return render(request,"sucess.html")


