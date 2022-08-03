from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    todo = Url.objects.all()
    if request.method == 'POST':
        new_Todu = Url(title = request.POST['title']).save()
        redirect('/')
    return render(request,'index.html',{'todo':todo})

def Delete(request,pk):
    todo = Url.objects.get(id = pk)
    todo.delete()
    return redirect('/')
