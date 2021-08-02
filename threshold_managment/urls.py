from django.urls import path
from .views import (

    TM_View,
    update_View,
    )


app_name = 'threshold_managment'

urlpatterns = [
    path('ThresholdManagment/', TM_View, name='TH'),
    path('ThresholdManagmentupdate/', update_View, name='update'),
]