from django.urls import path
from .views import (

    ED_View,
    Update_ED,

    )


app_name = 'ed_management'

urlpatterns = [
    path('ExtraDrill/', ED_View, name='ED'),
    path('ExtraDrill/<int:id>', Update_ED , name='update')
]