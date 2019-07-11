from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('api/user/create', views.UserCreate.as_view(), name='account-create'),
    path('api/test', views.Test.as_view(), name='test-view'),
]
