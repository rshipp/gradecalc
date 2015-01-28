from django.shortcuts import render
from gradecalc.models import Group

def index_view(request):
    groups = Group.objects.all()
    blah = groups[0].percentassignment_set.all()
    return render(request, 'gradecalc/index.html', {'groups': groups, 
        'blah': blah})
