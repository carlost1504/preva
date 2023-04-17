from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate

# Create your views here.
def home(request):
    #title='hello word'
    #return HttpResponse(title)
    return render(request, 'home.html')


def signup(request):

    if request.method=='GET':
        return render(request,'singup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                #regirter user
                user= User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tasks')
            except:
                return render(request,'singup.html',{
                    'form': UserCreationForm,
                    'error':'Username alredy exists'
                })
                 
        return render(request,'singup.html',{
            'form': UserCreationForm,
            'error':'Username alredy exists'
        })


    return render(request,'singup.html',{
        'form': UserCreationForm,
        'error':'Password do not match'
    })

def tasks(request):
    return render(request,'tasks.html')

def signout (request):
    logout(request)
    return redirect('home')

def signin(request):

    if request.method=='GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm
        })
    else:
        user= authenticate(
            request, username=request.POST['username'],password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html',{
            'form': AuthenticationForm,
            'error': 'username or password is incorrect'
            })
        else:
            login(request,user)
            return redirect('tasks')
        
    