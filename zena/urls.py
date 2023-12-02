from django.urls import path
from . import views

app_name = 'zena'
urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('announcements/', views.announcements, name='announcements')
]
