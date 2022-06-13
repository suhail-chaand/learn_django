from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError

from .models import BlogUser

# Register your models here.

class UserCreationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = BlogUser
        fields = ('email','phone','first_name','last_name')

    def clean_password_input(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('Passwords do not match')
        
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = BlogUser
        fields = ('email','phone','password','first_name','last_name')

class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('is_admin', 'first_name', 'last_name', 'email', 'phone', 'last_login', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        ('Contact',{'fields':('email','phone')}),
        ('Name',{'fields':('first_name','last_name')}),
        ('Info',{'fields':('password','is_admin')})
    )

    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('first_name', 'last_name', 'email','phone','password','confirm_password', 'is_admin')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(BlogUser, UserAdmin)
admin.site.unregister(Group)