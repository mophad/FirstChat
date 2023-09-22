
from django.contrib import admin
from .models import UserModel, User, Question , Choice

# Register your models he
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Choice)


# Register your models here.
