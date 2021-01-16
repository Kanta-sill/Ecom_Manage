from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from rest_framework import viewsets
from .models import Profile
from .serializers import UserSeri

# Create your views here.

def register(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, you are currently login')
            return redirect('login')
    else:
        form=RegisterForm()
    return render(request, 'user/register.html', {'form':form})

@login_required()
def profilepage(request):
    return render(request, 'user/profile.html')

class ProViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSeri