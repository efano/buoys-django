from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import requests

import pandas as pd
import json
from siphon.simplewebservice.ndbc import NDBC

from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# get data
df = NDBC.latest_observations()

# set the spatial extent to Great Lakes region
df = df.loc[df['latitude'].between(40.53, 49.15) & df['longitude'].between(
    -95.30, -74.36), ['latitude', 'longitude', 'station', 'time', 'wind_direction', 'wind_speed',
                      'wind_gust', 'wave_height', 'pressure', '3hr_pressure_tendency', 'air_temperature', 'water_temperature',
                      'dewpoint', 'visibility']].sort_values(by=['station'])

df = df.rename(columns={'3hr_pressure_tendency': 'pressure_tendency_3hr'})


def index(request):
    json_string = df.to_json(orient='records')
    data = json.loads(json_string)

    User = get_user_model()
    users = User.objects.all()
    comments = Comment.objects.all().order_by('-published_date')[:20]

    return render(request, 'buoys_app/index.html', {
        'data': data,
        'users': users,
        'comments': comments,
        'new_comment_form': NewCommentForm()
    })


@login_required
def new_comment(request):
    if request.method == 'POST':
        new_comment_form = NewCommentForm(request.POST)
        if new_comment_form.is_valid():
            comment = Comment()
            comment.user = request.user
            comment.buoy_id = request.POST['buoyID']
            comment.body = new_comment_form.cleaned_data['body']
            comment.save()

    return HttpResponseRedirect(reverse('buoys_app:index'))


@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id, user=request.user)
    comment.delete()
    return HttpResponseRedirect(reverse('buoys_app:index'))


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        profile_form = NewProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            #messages.success(request, 'Registration successful.')
            return redirect('buoys_app:index')
        messages.error(
            request, 'Unsuccessful registration. Invalid information.')
    else:
        form = NewUserForm()
        profile_form = NewProfileForm()

    return render(request, 'buoys_app/form_register.html', {'register_form': form, 'profile_form': profile_form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.info(request, f'You are now logged in as {username}.')
                return redirect('buoys_app:index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'buoys_app/form_login.html', {'login_form': form})


def logout_request(request):
    logout(request)
    # messages.info(request, 'You have successfully logged out.')
    return redirect('buoys_app:index')
