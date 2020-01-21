from django.urls import path

from . import views

app_name = 'airbnb'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.list, name='search'),
    path('search/<query>/', views.list, name='search'),
    #path('<str:pk>/', views.DetailView.as_view(), name='detail'),
]