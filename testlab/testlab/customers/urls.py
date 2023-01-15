from django.urls import path

from testlab.customers.views import CustomerCreateView, CustomerListView

urlpatterns = (
    path('', CustomerListView.as_view(), name='list customers'),
    path('add/', CustomerCreateView.as_view(), name='add customer'),
)
