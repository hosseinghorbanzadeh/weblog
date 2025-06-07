from django.urls import path,include
app_name='website'
from website.views import *

urlpatterns = [
    path('',index_view),
]
