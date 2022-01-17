from django.shortcuts import render
from electeur.models import Electeur

def index(request):
    elct = Electeur.objects.all()
    return render(request, 'index.html', {'elc': elct})
