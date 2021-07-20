from django.contrib import admin
from django.contrib import auth
from django.contrib.auth import admin as auth_admin
# Register your models here.
from .forms import UserCreationForm,UserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Informações Pessoais", {"fields": ("telegramID","telegramUser")}),
    )