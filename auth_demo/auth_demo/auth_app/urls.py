from django.urls import path

from auth_demo.auth_app.views import SignUpView, SignUpView2, sign_up_view, sign_in, SignInView, SignOutView

urlpatterns = (
    path('sign-up/', SignUpView2.as_view(), name='sign up'),
    path('sign-up-fbv/', sign_up_view, name='sign up fbv'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
)
