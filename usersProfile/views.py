from django.http.response import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, render, redirect
from .models import Users
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.renderers import JSONRenderer
from PIL import Image
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
from .forms import UserForm
from .forms import ProfileForm
def user_list(request):
    u= Users.objects.all()
    serializer = UserSerializer(u, many=True)
    print (serializer)
    json_data =  JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')

def user_detail(request,pk):
    u= Users.objects.get(id=pk)
    serializer = UserSerializer(u)
    print (serializer)
    json_data =  JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')

def home(request):
    if request.method == 'POST':
        form= UserForm(request.POST)
        if form.is_valid():
            #print(form)
            form.save()
            return redirect('login')

    form=UserForm()
    data=Users.objects.all()
    print(data)
    return render(request,'usersProfile/home.html',{'form': form,'data':data})


def home2(request):
    print("going inn")
    import pdb
    pdb.set_trace()
    u=Users(user=request.user)
    if request.method == 'POST':
        form= ProfileForm(request.POST, request.FILES, instance=u)
        data=Users.objects.all()
        if form.is_valid():
            key=request.user.id
            u.save()
            return render(request,'usersProfile/edit.html', {'form':form,'data':data, 'key':key})

    form= ProfileForm()
    return render(request,'usersProfile/home2.html', {'form':form})

def edit(request,pk):
    import pdb
    pdb.set_trace()
    u=Users(user=request.user)
    
    #taking id from auth user table to match with our users table whose data is to be edited
    if request.method == 'POST':
        auth= User.objects.filter(id=pk)
        _id=auth[0].users.id
        edit=Users.objects.get(id=_id)
        form= ProfileForm(request.POST, request.FILES, instance=u)
        try:
            if request.POST['save_name']:
                edit.name=request.POST['name']
        except:
            pass
        try:
            if request.POST['save_age']:
                edit.age=request.POST['age']
        except:
            pass
        try:
            if request.POST['save_skills']:
                edit.skills=request.POST['skills']
        except:
            pass
        try:
            if request.POST['save_image1']:
                edit.image1=request.FILES['image1']
        except:
            pass
        try:
            if request.POST['save_image2']:
                edit.image2=request.FILES['image2']
        except:
            pass
        edit.save()
        key=request.user.id
        data=Users.objects.all()
        return render(request,'usersProfile/home.html', {'form':form,'data':data, 'key':key})

    else:
        form= ProfileForm(instance=u)
    return render(request,'usersProfile/edit2.html', {'form':form})
    

