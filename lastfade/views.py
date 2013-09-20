# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from fader import fader

class BeginForm(forms.Form):
    username = forms.CharField(label="Pseudo Last.fm")
    limit = forms.IntegerField(label="Limite (200 max)", initial=200)

def home(request):
    results = None
    
    if request.GET.has_key('username'):
        form = BeginForm(request.GET)
    else:
        form = BeginForm()
    
    if form.is_valid():
        username = form.cleaned_data['username']
        limit = form.cleaned_data['limit']
        results = fader(username, limit)

    return render(request, "lastfade/index.html", {'form' : form, 'results' : results})
