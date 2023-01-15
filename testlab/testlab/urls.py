from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('testlab.common.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('testlab.accounts.urls')),
    path('customers/', include('testlab.customers.urls')),
    path('specifications/', include('testlab.specifications.urls')),
    path('tests/', include('testlab.validationtests.urls')),
]
