from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pools/', include('pools.urls')),
    path('admin/', admin.site.urls),
]