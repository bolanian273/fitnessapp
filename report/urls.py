from django.urls import path
from .views import create_report_view

app_name = 'report'

urlpatterns = [
    path('save/', create_report_view, name='create-report'),
    path('pdf/', create_report_view, name='pdf')
]
