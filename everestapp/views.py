from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import *

class ClientHomeView(TemplateView):
    template_name="clienthome.html"

class ClientAboutView(TemplateView):
    template_name="clientabout.html"

class ClientNewsView(ListView):
    template_name="clientnews.html"
    model= News
    context_object_name="news"

class ClientNewsDetailView(DetailView):
    template_name="clientnewsdetail.html"
    model= News
    context_object_name="newsdetail"

    '''def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        self.id=self.kwargs["pk"]
        news=news.objects.get(id=self.id)
        viewcount=news.viewed+1
        news.viewed=viewcount
        news.save()
        context["form"]=NewsCOmmentForm
        context["comments"]=Comment.objects.filter(post=news)
        return context'''




    