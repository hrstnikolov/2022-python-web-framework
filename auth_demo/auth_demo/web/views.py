from django.contrib.auth import models as auth_models, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render
from django.views import generic as views

# from auth_demo.auth_app.models import CustomUser

UserModel = get_user_model()

class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    context_object_name = 'users'
    model = UserModel
    template_name = 'index.html'

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     context_data['has_email'] = CustomUser.has_email(self.request.user)
    #
    #     return context_data