from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from useraccount.models import Profile
from django.core.exceptions import ValidationError

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField()   

    class Meta:
        model = User
        fields = [
            'username', 
            'email', 
            'password1', 
            'password2', 
            ]
             
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].help_text = "Your password must contain  10 characters."
        self.fields["username"].widget.attrs['placeholder'] = "Username"

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 10:
            raise ValidationError("Password must contain 10 character")
        return password
