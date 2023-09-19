from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from .forms import SignupForm
from django.contrib.auth import authenticate, login

 




def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Authentication successful, log the user in
            login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard page upon successful login
        else:
            # Authentication failed, show an error message
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')



def user(request):
    submitted =  False

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('{}?submitted=True'.format(reverse('login')))
        else:
            # If the form is not valid, you can handle this case as needed
            # For example, you can re-render the form with errors
            return render(request, 'user.html', {'form': form, 'submitted': submitted})

    else:
        form = SignupForm()

    # Ensure that there's a default response (e.g., rendering a template)
    return render(request, 'user.html', {'form': form, 'submitted': submitted})
   


def forgot(request):
    return render(request, 'forgot.html', {'name': 'hammed' })


def dashboard(request):
    return render(request, 'dashboard.html', {'name': 'hammed' })


