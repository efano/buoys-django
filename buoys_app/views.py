from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json
from siphon.simplewebservice.ndbc import NDBC
import requests


# get data
df = NDBC.latest_observations()

# set the spatial extent to Great Lakes region
df = df.loc[df['latitude'].between(40.53, 49.15) & df['longitude'].between(
    -95.30, -74.36), ['latitude', 'longitude', 'station']].sort_values(by=['station'])


def index(request):
    json_string = df.to_json(orient='records')
    data = json.loads(json_string)

    return render(request, 'buoys_app/index.html', {'data': data})


# def map(request):
#     json_string = df.to_json(orient='records')
#     data = json.loads(json_string)

#     return render(request, 'buoys_app/map.html', {'data': data})


# def sidebar(request):

#     return render(request, 'buoys_app/sidebar.html')
