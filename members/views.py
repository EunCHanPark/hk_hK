from django.shortcuts import render
from .models import Members
# Create your views here.

def index(request):
    members = Members.objects.all()

    return render(
        request,
        'members/index.html',
        {
            'members': members,
        }
)
