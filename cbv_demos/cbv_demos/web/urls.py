from django.urls import path
from django.views import generic as views

from cbv_demos.web.views import index, IndexView, IndexView2, FirstCBV, IndexViewWithTemplate2, IndexViewWithTemplate, \
    EmployeeListView, EmployeeDetailsView, EmployeeCreateView

urlpatterns = (
    path('', index, name='index'),
    path('1/', IndexView.get_index()),
    path('2/', IndexView2().index),
    path('3/', FirstCBV.as_view()),
    path('4/', IndexViewWithTemplate.as_view()),
    path('5/', IndexViewWithTemplate2.as_view()),
    path('list/', EmployeeListView.as_view(), name='employees list view'),
    path('employee/<int:pk>/', EmployeeDetailsView.as_view(), name='employee details view'),
    path('redirect_to_employees/', views.RedirectView.as_view(pattern_name='employees list view')),
    path('create-employee/', EmployeeCreateView.as_view()),
)