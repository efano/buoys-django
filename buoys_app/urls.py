from django.urls import path
from . import views


app_name = 'buoys_app'
urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('new/', views.new_comment, name='new_comment'),

]
