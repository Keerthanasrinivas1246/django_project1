from django.shortcuts import render,redirect

# user --> default model for authentication
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Register
def signup(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        if User.objects.filter(username = username).exists():
            messages.error(request,'Username already taken!...')
            return redirect('signup')
        
        if User.objects.filter(email = email).exists():
            messages.error(request,'email already used!...')
            return redirect('signup')

        else:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            messages.success(request,'User registered Successfully!...')
            return redirect('signin')
    return render(request,'signup.html')

#Login
def signin(request):
    if request.method =='POST':
        user = authenticate(request,
                            username = request.POST['username'],
                            password = request.POST['password']
        )
        if user:
            login(request,user)
            messages.success(request,'User logged in succesfully!...')
            return redirect('read_article')
        else:
            messages.info(request,'invalid credentials')
            return redirect('signin')
    return render(request,'signin.html')

#Profile
@login_required(login_url='signin')
def profile(request):
    user = request.user # it will detect and fetch the currently active user 
    return render(request,'profile.html', {'keeru': user})

#update_profile
@login_required(login_url='signin')
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        user.first_name= request.POST['first_name']
        user.last_name= request.POST['last_name']
        user.email= request.POST['email']
        user.username= request.POST['username']
        user.save()
        messages.success(request,'User profile updated successfully!....')
        return redirect('profile')
    return render(request,'update_profile.html',{ 'keeru': user })

#update_pwd
@login_required(login_url='signin')
def update_password(request):
    user = request.user
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if not user.check_password(current_password):
            messages.error(request,'Current password is invalid!...')
            return redirect('update_password')
        elif new_password == current_password:
            messages.error(request,'Old password and new password are same !...')
            return redirect('update_password')
        elif new_password != confirm_password:
            messages.error(request,'confirm password and new password are different !...')
            return redirect('update_password')
        else:
            user.set_password(new_password) 
            user.save()  
            update_session_auth_hash(request,user)
            messages.success(request,'User password updated successfully!...')
            return redirect('profile')
    return render(request,'update_password.html')

# logout
@login_required(login_url='signin')
def signout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'User logged out successfully!...')
        return redirect('signin')
    return render(request,'signout.html')


