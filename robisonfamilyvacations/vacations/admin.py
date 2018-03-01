from django import forms
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
# from django.contrib.auth.forms import 
from .models import vacation

admin.site.register(vacation)
