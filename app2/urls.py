from app2.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('bank2/',bank2,name='bank2'),
]