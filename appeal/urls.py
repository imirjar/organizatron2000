from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from .views import *



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	path('', appeal),
	path('<int:appeal_id>', appeal_detail),
    path('appeal_list/', appeal_list),
    path('appeal_create/', appeal_create),
]