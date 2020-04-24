from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    #path('data/', views.get_data, name='api-data'),
    path('api/data/', views.apidata, name='apidata'),
    path('upload/', views.upload, name='upload'),
    path('form/', views.model_form_upload, name='model_form_upload')

]