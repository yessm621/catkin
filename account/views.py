from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.models import CatkinUser


class AccountRegisterView(CreateView):
    model = CatkinUser
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/register.html'
