from django.contrib import admin
from django.urls import path, include
from backend.views import analyze_code

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('allauth.urls')),
    path('api/analyze/', analyze_code, name='analyze_code'),
]
    