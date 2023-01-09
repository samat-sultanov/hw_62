from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from accounts.forms import MyUserCreationForm
from django.views.generic import CreateView


class RegisterView(CreateView):
    model = User
    form_class = MyUserCreationForm
    template_name = 'user_create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url

        next_url = self.request.POST.get('next')
        if next_url:
            return next_url

        return reverse('webapp:index')