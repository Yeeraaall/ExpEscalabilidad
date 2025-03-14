from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('imgmris/', views.imgmri_list),
    path('imgmricreate/', csrf_exempt(views.imgmri_create), name='imgmriCreate'),
]