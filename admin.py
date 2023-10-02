
from django.contrib import admin
from .models import UserModel, User, Question , Choice, Article,Page_Setting, Create_Acct , Create_Company, Open_Ai ,Bot_Acct

# Register your models he
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Article)
admin.site.register(Page_Setting)
admin.site.register(Create_Acct)
admin.site.register(Create_Company)
admin.site.register(Open_Ai)
admin.site.register(Bot_Acct)




# Register your models here.
