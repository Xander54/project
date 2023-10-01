from django.urls import path
from . import views
from .views import Userpage,Index,Data
urlpatterns = [
    path('user/',Userpage.as_view(),name='user'),
    path('time_line/',Index.as_view(),name='time_line'),
    path("",Data.as_view(),name="form")
    ]
