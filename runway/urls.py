from django.contrib import admin
from django.urls import include, path

urlpatterns=[
    path("runwaymaster/", include("master.urls")),
    path("runwaymaster/admin/",admin.site.urls),
]
