from django.shortcuts import render, redirect
from .models import Stock




def accounts(response):
    form = UserCreationForm()
    return render(response, 'accounts/accounts.html', {'form':form})