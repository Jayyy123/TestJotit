from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import Jotter,Addjotter


def home(request):
    return render(request,'taj/home.html')

def jotters(request):
    jotters = Jotter.objects.all()

    return render(request,'taj/jotters.html',{'a':jotters})

def add_jotters(request):
    newJotter = Addjotter()
    if request.method == 'POST':
        newJotter = Addjotter(request.POST)
        if newJotter.is_valid():
            newJotter.save()
            messages.success(request,"{} has been successfully saved".format(request.POST['title']))
            return redirect('jotters')
        else:
            messages.error(request,"An error occured and {} could not be saved!".format(request.POST['title']))
    
    return render(request,'taj/add_jotter.html',{'a':newJotter})

def edit_jotters(request,pk):
    selectedJotter = Jotter.objects.get(id=pk)
    newJotter = Addjotter(instance = selectedJotter)
    if request.method == 'POST':
        newJotter = Addjotter(request.POST, instance = selectedJotter)
        if newJotter.is_valid():
            newJotter.save()
            messages.success(request,"{} has been updated successfully!".format(request.POST['title']))
            return redirect('jotters')
        else:
            messages.error(request,"There was an error  and {} could not be updated!")

    return render(request,'taj/edit_jotters.html', {'a':newJotter})

def jotter(request,pk):
    selectedJotter = Jotter.objects.get(id=pk)
    
    return render(request, 'taj/jotter.html', {'a':selectedJotter})

