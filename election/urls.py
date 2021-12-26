from django.contrib import admin
from django.urls import include, path


admin.site.site_header= "Administration | ISI Election |"




urlpatterns = [
    path('condidat/', include('condidat.urls')),
    path('admin/', admin.site.urls),
]