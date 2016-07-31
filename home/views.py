from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView, ListView, FormView, UpdateView
# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"