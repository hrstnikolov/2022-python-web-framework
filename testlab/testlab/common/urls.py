from django.urls import path

from testlab.common.views import index

urlpatterns = (
    path('', index, name='index'),
)