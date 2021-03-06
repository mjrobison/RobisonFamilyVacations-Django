from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.shortcuts import render

from .models import Vacation
from robisonfamilyvacations.users.models import User

class VacationListView(LoginRequiredMixin, ListView):
    model = Vacation

    slug_field = 'vacation'
    slug_url_kwarg = 'vacation'
