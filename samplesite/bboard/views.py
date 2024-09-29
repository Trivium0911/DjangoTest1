from django.shortcuts import render
from .models import Bd, Rubric


def index(request):
    database = Bd.objects.all()
    rubrics = Rubric.objects.all()
    context = {'database': database, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)


def rubric_bds(request, rubric_id):
    database = Bd.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'database': database, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/rubric_bds.html', context)

