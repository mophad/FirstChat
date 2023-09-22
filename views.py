from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.contrib.auth.models import User
from django.contrib import messages 

 
def user(request):
    

    if request.method == "POST":
        fullname = request.POST["fullname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = fullname
        user.save()
        return render(request, 'user1.html', {'msg' : 'Your Acount have been created successfuly' })

    
        # messages.success(request, 'Registration successful. You can now log in.')
        # return redirect('signup:login')  
    
    else:
            
            return render(request, 'user1.html',)








#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             submitted = True
#             return redirect('{}?submitted=True'.format(reverse('signup:login')))
#         else:
            # If the form is not valid, you can handle this case as needed
            # For example, you can re-render the form with errors
            # return render(request, 'user.html', {'form': form, 'submitted': submitted})

    # else:
        # form = SignupForm()

    # Ensure that there's a default response (e.g., rendering a template)
    # return render(request, 'user.html', {'form': form, 'submitted': submitted})
   



def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username= email, password=password)

        if user is not None:
            # Authentication successful, log the user in
            login(request, user)
            return redirect('signup:home')  
        else:
            # Authentication failed, show an error message
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')



# def user(request):
    # submitted =  False

    # if request.method == "POST":
        # form = SignupForm(request.POST)
        # if form.is_valid():
            # form.save()
            # submitted = True
            # return redirect('{}?submitted=True'.format(reverse('signup:login')))
        # else:
            # If the form is not valid, you can handle this case as needed
            # For example, you can re-render the form with errors
            # return render(request, 'user.html', {'form': form, 'submitted': submitted})

    # else:
        # form = SignupForm()

    # Ensure that there's a default response (e.g., rendering a template)
    # return render(request, 'user.html', {'form': form, 'submitted': submitted})
   


def forgot(request):
    return render(request, 'forgot.html', {'name': 'hammed' })


def dashboard(request):
    user_name = request.user.first_name if request.user.is_authenticated else None
    return render(request, 'dashboard.html', {'user_nme': user_name })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist ):
        # Redisplay the question voting form.
        return render(
            request,
            "test.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("signup:vote", args=(question.id,)))