from django.contrib.auth import authenticate, login, views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render


@login_required(login_url=reverse_lazy('teams:login'))
def index(request):
    context = {'username': request.user.get_username()}

    return render(request, 'teams/index.html', context)
