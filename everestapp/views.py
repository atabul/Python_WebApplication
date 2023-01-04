from django.shortcuts import render
from django.views.generic import View, TemplateView


class ClientHomeView(TemplateView):
    template_name="clienthome.html"

class ClientAboutView(TemplateView):
    template_name="clientabout.html"




    