from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import forms as auth_forms, authenticate, login, logout, get_user_model
from django.contrib.auth import views as auth_views

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from auth_demo.auth_app.forms import SignUpForm, SignInForm

UserModel = get_user_model()

# # Simplest, shows all model fields in the form
# class SignUpView(views.CreateView):
#     model = User
#     fields = '__all__'
#     template_name = 'auth/sign-up.html'

# Better, but uses the build-in `UserCreationForm` and can't be extended
class SignUpView(views.CreateView):
    form_class = auth_forms.UserCreationForm
    template_name = 'auth/sign-up.html'


# The default way to create registration view - using custom form which inherits from `UserCreationForm`
class SignUpView2(views.CreateView):
    form_class = SignUpForm
    template_name = 'auth/sign-up.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


# Same as above but using FBV
def sign_up_view(request):
    if request.method == 'GET':
        form = SignUpForm()
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign up')

    context = {
        'form': form,
    }

    return render(request, 'auth/sign-up.html', context)


def sign_in(request):
    if request.method == 'GET':
        form = SignInForm()
    else:
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # user = authenticate(request, username=username, password=password)
            user = authenticate(request, **form.cleaned_data)
            if user:
                login(request, user)

    context = {
        'form': form,
    }

    return render(request, 'auth/sign-in.html', context)


class SignInView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return self.get_redirect_url() or self.get_default_redirect_url()



class SignOutView(auth_views.LogoutView):
    pass
