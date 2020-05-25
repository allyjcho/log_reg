from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def success(request):
    if 'name' in request.session:
        context = {
            'all_messages': Message.objects.all()
        }
        return render(request, 'success.html', context)
    return redirect('/')

def register(request):
    # create a new user
    # validate the post data
    print(request.POST)
    errors = User.objects.validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    hashed_password = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=hashed_password)
    print(new_user, "This is my new user!")
    request.session['name'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect('/success')

def login(request):
    # see if POST data matches a user from db
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user)>0:
        logged_user = logged_user[0]
        if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.password.encode()):
            print(logged_user, "logged user was signed in")
            request.session['name'] = logged_user.first_name
            request.session['id'] = logged_user.id
            return redirect('/success')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def create_msg(request):
    if request.method == 'POST':
        new_msg = Message.objects.create(message=request.POST['message'], poster=User.objects.get(id=request.session['id']))
        print(new_msg, "NEW MESSAGE WAS POSTED")
        return redirect('/success')
    return redirect('/')

def add_cmt(request, msg_id):
    if request.method == 'POST':
        new_cmt = Comment.objects.create(comment=request.POST['comment'], poster=User.objects.get(id=request.session['id']), message=Message.objects.get(id=msg_id))
        print(new_cmt)
        return redirect('/success')
    return redirect('/')