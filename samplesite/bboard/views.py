from django.shortcuts import render
from .models import Bd


def index(request):
    database = Bd.objects.all()
    return render(request, 'bboard/index.html', {'database': database})


