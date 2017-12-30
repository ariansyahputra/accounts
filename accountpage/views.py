from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required


@login_required
def test_view(request):
    context = {
        'user': request.user,
    }
    return render(request, 'accountpage/profile.html', context)
