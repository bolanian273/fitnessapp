from django.urls import path
from .views import ( 
    home_view,
    fitness_list_view,
    fitness_detail_view,
    UploadTemplateView,
    csv_upload_view
    )

app_name = 'fitness_analyser'

urlpatterns = [
    path('', fitness_list_view, name='home'),
    path('fitness/', fitness_list_view, name='list'),
    path('upload/',UploadTemplateView.as_view(), name='upload'),
    path('csv/', csv_upload_view, name='csv'),
    path('fitness/detail/<int:id>', fitness_detail_view, name='detail')
]
