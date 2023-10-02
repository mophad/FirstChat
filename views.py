from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse
from .forms import App_Customize, Create_User, Bot_Set, Open_Ai_Acct, Create_Company_Acct
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice, Article, Create_Acct
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


def display_article(request):
    article = Article.objects.all()
    return render(request, 'article.html' ,{'article' : article})


def save_article(request):
    if request.method =="POST":
        title = request.POST["title"]
        message = request.POST["message"]
        article = Article()
        article.title = title
        article.boytext = message
        article.save()
        return redirect('signup:read_article')
    # else:
        # return render(request,'write_article.html') 
    
    return render(request,'write_article.html')
    

def delete_article(request, update_id ):
    article = Article.objects.get(pk = update_id)
    article.delete()
    return render(request,'article.html', )


def appsetting(request):
     if request.method == "POST":
         form = App_Customize(request.POST)
         if form.is_valid():
             form.save()
             form = App_Customize()           

            #  return redirect('{}?submitted=True'.format(reverse('signup:login')))
             msg = "you have been successfuly update your App"
             return render(request, 'custome.html', {'msg': msg , 'form' : form})

         else:
             form = App_Customize()           
             msg = "there was error of input detail"
             return render(request, 'custome.html', { 'msg': msg , 'form' : form})

     else:
         form = App_Customize()           
    # Ensure that there's a default response (e.g., rendering a template)
     return render(request, 'custome.html', {'form': form})
   
def chatbot(request):
    return render(request , 'bot.html' )

def lead(request):
    return render(request , 'lead.html' )

def setting(request):
    return render(request , 'setting.html' )


def chatboard(request):
    return render(request , 'chat.html' )

def forgot(request):
    return render(request, 'forgot.html', {'name': 'hammed' })

def botsetting(request):
     if request.method == "POST":
         form = Bot_Set(request.POST)
         if form.is_valid():
             form.save()
             form = Bot_Set()           

            #  return redirect('{}?submitted=True'.format(reverse('signup:login')))
             msg = "you have been successfuly update your App"
             return render(request, 'botset.html', {'msg': msg , 'form' : form})

         else:
             form = Bot_Set()           
             msg = "there was error of input detail"
             return render(request, 'botset.html', { 'msg': msg , 'form' : form})

     else:
         form = Bot_Set()           
    # Ensure that there's a default response (e.g., rendering a template)
     return render(request, 'botset.html', {'form': form})




def integrat(request):
    if request.method == "POST":
         form = Open_Ai_Acct(request.POST)
         if form.is_valid():
             form.save()
             form = Open_Ai_Acct()           

            #  return redirect('{}?submitted=True'.format(reverse('signup:login')))
             msg = "you have been successfuly update your App"
             return render(request, 'intergrate.html', {'msg': msg , 'form' : form})

         else:
             form = Open_Ai_Acct()           
             msg = "there was error of input detail"
             return render(request, 'intergrate.html', { 'msg': msg , 'form' : form})

    else:
         form = Open_Ai_Acct()           
    # Ensure that there's a default response (e.g., rendering a template)
    return render(request, 'intergrate.html', {'form': form})


# def custome_app(request):
#     return render(request, 'custome.html', {'name': 'hammed' })

def add_user(request):
     if request.method == "POST":
         form = Create_User(request.POST)
         if form.is_valid():
             form.save()
             form = Create_User()           

            #  return redirect('{}?submitted=True'.format(reverse('signup:login')))
             msg = "you have been successfuly update your App"
             return render(request, 'add_user.html', {'msg': msg , 'form' : form})

         else:
             form = Create_User()           
             msg = "there was error of input detail"
             return render(request, 'add_user.html', { 'msg': msg , 'form' : form})

     else:
         form = Create_User()           
    # Ensure that there's a default response (e.g., rendering a template)
     return render(request, 'add_user.html', {'form': form})



def add_company(request):
    return render(request, 'company.html', {'name': 'hammed' })
     

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
