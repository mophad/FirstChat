from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "signup"
 
urlpatterns = [
    path('' ,views.login_view , name ='login'),
    path('user', views.user, name='user'),
    path('forgot', views.forgot, name='forgot'),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('home', views.dashboard, name='home'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
 path('bot', views.chatbot, name='bot'),
    path('chat', views.chatboard, name='chat'),
    path('lead', views.lead, name='lead'),
    path('setting', views.setting, name='setting'),
    path('set_bot', views.botsetting, name='set_bot'),
    path('set_app', views.appsetting, name='set_app'),
    path('integrate', views.integrat, name='integrate'),
    path('add_user', views.add_user, name='add_user'),
    path('add_company', views.add_company, name='add_company'),
    # path('customize', views.custome_app, name='customize'),



]
