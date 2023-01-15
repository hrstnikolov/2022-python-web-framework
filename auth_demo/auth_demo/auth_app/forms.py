from django import forms
from django.contrib.auth.forms import UsernameField
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()

class SignUpForm(auth_forms.UserCreationForm):
    age = forms.CharField()
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    class Meta:
        model = UserModel
        fields = ('email',)


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
