from django.shortcuts import render
from gradecalc.models import PointsCourse, PercentCourse

def index_view(request):
    courses = list(PointsCourse.objects.all()) + list(PercentCourse.objects.all())
    return render(request, 'gradecalc/index.html', {'courses': courses})
