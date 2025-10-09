from django.views import generic
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .models import User
from .forms import RegisterForm, LoginForm

class RegisterView(generic.CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = '/auth/login/'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    success_url = '/'


    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    