from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import json
from siphon.simplewebservice.ndbc import NDBC
import requests
from .forms import *


# get data
df = NDBC.latest_observations()

# set the spatial extent to Great Lakes region
df = df.loc[df['latitude'].between(40.53, 49.15) & df['longitude'].between(
    -95.30, -74.36), ['latitude', 'longitude', 'station', 'time', 'wind_direction', 'wind_speed', 'wind_gust', 'wave_height', 'pressure', '3hr_pressure_tendency', 'air_temperature', 'water_temperature', 'dewpoint', 'visibility', 'water_level_above_mean', 'dominant_wave_period', 'average_wave_period']].sort_values(by=['station'])

df = df.rename(columns={"3hr_pressure_tendency": "pressure_tendency_3hr"})


def index(request):
    json_string = df.to_json(orient='records')
    data = json.loads(json_string)

    return render(request, 'buoys_app/index.html', {'data': data})
