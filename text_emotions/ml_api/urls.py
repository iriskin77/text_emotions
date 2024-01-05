from django.urls import path
from .views import FileApiList, download_file, upload_file, process_file

urlpatterns = [
    path('fileslist/', FileApiList.as_view()),
    path('fileslist/<int:pk>/', FileApiList.as_view()),
    path('download_file/<int:pk>', download_file, name='file_download'),
    path('upload_file/', upload_file, name='upload_file'),
    path('process_file/<int:pk>', process_file, name='process_file')
]
