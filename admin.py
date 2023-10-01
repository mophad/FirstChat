
from django.contrib import admin
from .models import UserModel, User, Question , Choice, Article , Page_Setting

# Register your models he
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Article)
admin.site.register(Page_Setting)



# Register your models here.
