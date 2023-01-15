from django.urls import path

from auth_demo.web.views import UsersListView

urlpatterns = [
    path('', UsersListView.as_view(), name='index'),
]