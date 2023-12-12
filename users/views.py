import os

import stripe
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from content_app.services import create_product, create_price, create_session
from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/user_form.html'

    def get_success_url(self):
        return reverse_lazy('content_app:home')

    def form_valid(self, form):
        stripe.api_key = os.getenv('STRIPE_API_KEY')
        product = create_product('Content-Plus')
        price = create_price(product, 200)
        session = create_session(price)
        return redirect(session['url'])
