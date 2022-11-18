from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("entries/", include("entries.urls")),
    path("artballot/", include("entries.urls")),
]
