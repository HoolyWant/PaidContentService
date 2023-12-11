from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from content_app.models import Publication, Channel, Subscription


class PublicationView(LoginRequiredMixin, DetailView):
    model = Publication


class PublicationCreate(LoginRequiredMixin, CreateView):
    model = Publication

    def form_valid(self, form):
        self.object = form.save()
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)


class ChannelList(ListView):
    model = Channel


class ChannelCreate(CreateView):
    model = Channel

    def form_valid(self, form):
        self.object = form.save()
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)


class ChannelView(DetailView):
    model = Channel

    def get_context_data(self, **kwargs):
        context = super(ChannelView, self).get_context_data(**kwargs)
        if self.request.user.is_subscribed or self.request.user.is_staff:
            context['publications'] = Publication.objects.filter(channel_id=self.get_object().id)
        else:
            context['publications'] = Publication.objects.filter(
                                                                channel_id=self.get_object().id).filter(
                                                                is_free=True)
        try:
            context['subscription'] = Subscription.objects.get(user_id=self.request.user.id, channel_id=self.get_object().id).__dict__['subscription_status']
            return context
        except Exception:
            return context

    def post(self, request, **kwargs):
        self.object = self.get_object()
        if request.POST.get('button'):
            user = request.user
            try:
                subscription = Subscription.objects.get(user_id=user.id, channel_id=self.object.id)
                if subscription.__dict__['subscription_status']:
                    subscription.subscription_status = False
                    subscription.save()
                else:
                    subscription.subscription_status = True
                    subscription.save()
                return redirect('content_app:success')
            except Exception:
                Subscription.objects.create(user_id=user.id, channel_id=self.object.id, subscription_status=True)
                return redirect('content_app:success')
        context = self.get_context_data(object=self.object)
        return render(request, context)


class PublicationDetail(DetailView):
    model = Publication


def sub_success(request):
    if request.method == 'GET':
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def home(request):
    return render(request, 'content_app/home.html')


