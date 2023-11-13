from django.shortcuts import render, redirect

from .forms import updat
from .models import movie_details
# Create your views here.
def index(request):
    obj=movie_details.objects.all()
    return render(request,'index.html',{'ob':obj})

def details(request,m_id):
    mov=movie_details.objects.get(id=m_id)
    return render(request,'details.html',{'movie':mov})

def add_movie(request):

    if request.method=='POST':
        movi=request.POST.get('movie',)
        im= request.FILES['img']
        yr = request.POST.get('year',)
        des = request.POST.get('des',)

        mv=movie_details(name=movi,im=im,year=yr,des=des)
        mv.save()

    return render(request,'add.html')

def update(request,id):
    mo=movie_details.objects.get(id=id)
    form=updat(request.POST or None,request.FILES,instance=mo)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'movie':mo,'form':form})

def delete(request,id):
    if request.method=='POST':
        mov=movie_details.objects.get(id=id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')