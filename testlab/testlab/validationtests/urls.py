from django.urls import path, re_path

from testlab.validationtests.views import ValidationTestListView, ValidationTestCreateView

urlpatterns = (
    path('', ValidationTestListView.as_view(), name='list validation tests'),
    path('add/', ValidationTestCreateView.as_view(), name='add validation test'),
)