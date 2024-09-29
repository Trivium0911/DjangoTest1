from django.urls import path
from .views import index, rubric_bds

urlpatterns = [
    path('<int:rubric_id>/', rubric_bds),
    path('', index),
]
