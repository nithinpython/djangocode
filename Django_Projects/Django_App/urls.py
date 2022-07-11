from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo'),
    # path('resu/',views.Arithmetic,name='Arithmetic'),


]
