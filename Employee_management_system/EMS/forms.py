from django import forms
from django.contrib.auth.forms import UserCreationForm
from EMS.models import User
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    fname = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    email = forms.CharField(
        widget= forms.EmailField(
            attrs={
                "class": "form-control"
            }
        )
    )

    passd = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    cpass = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('username', 'fname', 'email', 'passd', 'cpass', 'is_admin', 'is_sales', 'is_production', 'is_devloper', 'is_client')
