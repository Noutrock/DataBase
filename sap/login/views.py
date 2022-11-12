from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from login.forms import formRegister


def register(request):
    if request.method == 'POST':
        form = formRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
        return redirect('login')

    else :
            form = formRegister()
    return render(request,'registro.html',{'form':form})

