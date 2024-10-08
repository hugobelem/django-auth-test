from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name='pages/home.html'), name="home"),
    path('admin/', admin.site.urls),
    path("accounts/", include('accounts.urls')),
    path("accounts/", include('django.contrib.auth.urls')),
    path("perfil/", include('perfil.urls'), name="perfil"),
]
 