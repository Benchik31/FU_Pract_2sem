from django import forms
from .models import User
from django.core.exceptions import ValidationError

from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        #Add fields we will be collecting info for
        fields = ['first_name','last_name','username', 'email', 'password']

    #DO form cleanig here
    def clean_username(self):
        username = self.cleaned_data['username']
        if  User.objects.filter(username = username).exists():
            raise ValidationError('Username is not available')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')

        #check password length
        if len(password) < 8:
            raise ValidationError("Password can't be less than 8 characters")
        #check for number and letters is password
        if password.isalpha() or password.isnumeric():
            raise ValidationError("Password should contains both letters and numbers")

        return password

# class SignUpForm(UserCreationForm):
#
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username', 'email', 'password']

class Loginform(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


