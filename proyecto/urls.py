
from django.contrib import admin
from django.urls import path
from proyecto.views import hola_mundo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/',hola_mundo)
]
