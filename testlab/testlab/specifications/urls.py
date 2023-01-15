from django.urls import path, re_path, include

from testlab.specifications.views import SpecificationListView, SpecificationCreateView, SpecificationDetailsView, \
    SpecificationListByCustomerView

urlpatterns = (
    path('', SpecificationListView.as_view(), name='list specifications'),
    path('<int:pk>/', SpecificationDetailsView.as_view(), name='details specification'),
    path('add/', SpecificationCreateView.as_view(), name='add specification'),
    path('customer/<str:cust>/', include([
        path('', SpecificationListByCustomerView.as_view(), name='list by customer specifications'),
    ])),
)