from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User


class UsAdmin(UserAdmin):
    pass


admin.site.register(User, UsAdmin)
