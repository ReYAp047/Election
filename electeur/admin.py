from django.contrib import admin

# Register your models here.

from condidat.models import *
from electeur.models import Electeur

admin.site.register([Electeur])