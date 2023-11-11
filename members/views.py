from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Can't call this login, or we'll get a conflict from the import.
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else: 
            messages.success(request, 'Incorrect username and password combination, please try again.')
            return redirect('login')

    else:
        return render(request, 'authentication/login.html', {})
    
def logout_user(request):
    logout(request)

    messages.success(request, 'Logout successful.')
    return redirect('login')