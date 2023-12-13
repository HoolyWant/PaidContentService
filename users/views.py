import os

import stripe
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, DetailView

from content_app.models import Payment
from content_app.services import create_product, create_price, create_session
from users.forms import UserRegisterForm, UserLoginForm
from users.models import User

stripe.api_key = os.getenv('STRIPE_API_KEY')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse_lazy('content_app:home')

    def form_valid(self, form):
        product = create_product('ContentPlus')
        price = create_price(product, 200)
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": price,
                    "quantity": 1,
                },
            ],
            metadata={
                "user_id": form.instance.id
            },
            mode="subscription",
            success_url=os.getenv('YOUR_DOMAIN') + '/users/success/',
            cancel_url=os.getenv('YOUR_DOMAIN') + '/users/cancel/',
        )
        Payment.objects.create(user_id=form.instance.id, session_id=session['id'])
        form.save()
        return redirect(session['url'])


class SuccessView(TemplateView):
    template_name = 'users/success.html'

    def post(self, request):
        phone_number = request.POST.get
        user = User.objects.get(phone_number=phone_number)
        session_id = Payment.objects.get(user_id=user.id).session_id
        session = stripe.checkout.Session.retrieve(
                session_id,
            )
        if session['payment_status']:
            user.is_active = True
            user.save()
            payment = Payment.objects.get(user=user)
            payment.success = True
            payment.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return reverse_lazy('users:cancel')

    def get_success_url(self):
        return reverse_lazy('content_app:home')


class CancelView(TemplateView):
    template_name = "cancel.html"



