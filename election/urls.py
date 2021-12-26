from django.contrib import admin
from django.urls import include, path
from condidat.views import index


admin.site.site_header= "Administration | ISI Election |"

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name='index-page'),
]