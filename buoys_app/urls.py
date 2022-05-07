from django.urls import path

from . import views


urlpatterns = [

    path('', views.index, name='index'),
    # path('buoys/', views.sidebar, name='sidebar'),
    # path('buoys/map/', views.map, name='map')
]
