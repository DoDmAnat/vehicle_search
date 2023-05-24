
from django.contrib import admin
from django.urls import path, include

import cargos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("cargos.urls"))
]
