from dataclasses import fields
from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class userRegisterForm(UserCreationForm):
    # password1 = forms.CharField.(label = 'Constraseña', widget = forms.PasswordInput)
    """ password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    ) """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required' : '',
            'id' : 'username',
            'type': 'text',
            'class' : 'form-control',
            'placeholder' : 'John Lenon',
            'maxlength' : '16',
            'minlengt' : '6',
        })
        self.fields["password1"].widget.attrs.update({
            'required' : '',
            'id' : 'username',
            'type': 'password',
            'class' : 'form-control',
            'placeholder' : 'John Lenon',
            'maxlength' : '16',
            'minlengt' : '6',
        })
        self.fields["password2"].widget.attrs.update({
            'required' : '',
            'id' : 'username',
            'type': 'password',
            'class' : 'form-control',
            'placeholder' : 'John Lenon',
            'maxlength' : '16',
            'minlengt' : '6',
        })
    class Meta:
        model = User
        fields = ("username","password1", "password2")
        help_text = {k:"" for k in fields}
class loginUserForm(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super().__init__ (*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required' : '',
            'id' : 'username',
            'type': 'password',
            'class' : 'form-control',
            'placeholder' : 'John Lenon',
            'maxlength' : '16',
            'minlengt' : '6',
        })
        self.fields["password"].widget.attrs.update({
            'required' : '',
            'id' : 'username',
            'type': 'password',
            'class' : 'form-control',
            'placeholder' : '********',
            'maxlength' : '16',
            'minlengt' : '6',
        })
        
    class Meta:
        model = User
        fields = ("username", "password")
        help_text = {i:"" for i in fields}