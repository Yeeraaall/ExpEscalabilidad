from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('eventos/', views.evento_list),
    path('eventocreate/', csrf_exempt(views.evento_create), name='eventoCreate'),
]