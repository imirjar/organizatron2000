from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from .views import *



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	path('', appeal),#стартовая страница без функционала
    path('appeal_list/', appeal_list),#список всех обращений в таблице django_Appeal
    path('appeal_create/', appeal_create),#заполнить основные параметра требуемые для ответа
    path('appeal_edit/<int:appeal_id>', appeal_edit),#пока только редактирование ОТВЕТА на обращение
    path('appeal_archive/<int:appeal_id>', appeal_archive),
    path('appeal_accept/<int:appeal_id>', appeal_accept),#подтвержденная правильность ответа(в основном для стилей темплейта)
    path('appeal_generate/<int:appeal_id>', appeal_generate),#подтверждение создания docx файла
]