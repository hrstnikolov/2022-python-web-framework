from django.urls import path

from testlab.accounts.views import SignUpView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
)