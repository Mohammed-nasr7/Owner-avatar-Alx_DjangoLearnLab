from django.urls import path
from .views import RegisterView, LoginView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  
]
