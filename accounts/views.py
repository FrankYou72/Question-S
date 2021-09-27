from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import RedirectView
from .forms import UserCreationFormWithEmail
from django.contrib.auth.models import User



class SignupView(generic.CreateView):
    success_url = reverse_lazy('login')

    def get(self, request):
        print('get')
        form = UserCreationFormWithEmail()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationFormWithEmail(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('Form is valid')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user = User()
            user.username = form.cleaned_data.get('username')
            user.email = form.cleaned_data.get('email')
            user.password = form.cleaned_data.get('password')
            user.password2 = form.cleaned_data.get('password2')
            user.save()
            
            print('yay')
            return reverse_lazy('login')
            
        else:
            print('Form is not valid')
            return self.get(request)



# Create your views here.
