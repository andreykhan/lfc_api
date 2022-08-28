from django.contrib import admin
from django.urls import path, include
from .schema import schema


urlpatterns = [
    path('', schema),
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls'))
]
