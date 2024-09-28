from django.shortcuts import render
from .models import Bd


def index(request):
    database = Bd.objects.order_by('-published')
    return render(request, 'bboard/index.html', {'database': database})


