from django.shortcuts import render
from condidat.models import Condidat


def index(request):
    cond = Condidat.objects.all()
    return render(request, 'index.html', {'con': cond})