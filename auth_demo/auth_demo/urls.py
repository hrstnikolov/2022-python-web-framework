from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('auth_demo.auth_app.urls')),
    path('', include('auth_demo.web.urls')),
]
