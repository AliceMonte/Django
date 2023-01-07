from django.urls import path
from . import views

urlpatterns = [
path('', views.index),
path('about/',views.about),
path('contacts/',views.contacts),
path('about/<user>',views.user),
path('about/<user>/<int:age>',views.user),
path('contacts',views.contact)
]