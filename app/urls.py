from django.contrib import admin
from django.urls import path
from .views import UserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserAPIView.as_view()),
]