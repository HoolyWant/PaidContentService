from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from content_app.models import Publication, Channel


class PublicationView(LoginRequiredMixin, DetailView):
    model = Publication


class PublicationCreate(LoginRequiredMixin, CreateView):
    model = Publication


class ChannelList(ListView):
    model = Channel


class ChannelCreate(CreateView):
    model = Channel

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner_id = self.request.user


class ChannelView(DetailView):
    model = Channel

    def get_context_data(self, **kwargs):
        context = super(ChannelView, self).get_context_data(**kwargs)
        context['publications'] = Publication.objects.filter(channel_id=self.get_object().id)
        return context



def home(request):
    pass
