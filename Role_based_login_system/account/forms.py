from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, File_1

choice_1 = [('asd', 'asdas'),('asdads', 'a21sdas') ]

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    designation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'number', 'is_admin', 'designation', 'is_sales', 'is_production', 'is_devloper', 'is_client', 'roles')

class FilesN(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     ))
    # file = forms.FileField(widget=forms.FileInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     ))
    # description = forms.CharField(widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control"
    #         }
    #     ))
    class Meta:
        model = File_1
        fields = ('file', 'title', 'description', 'is_admin_file', 'is_sales_file', 'is_production_file', 'is_devloper_file', 'is_client_file')