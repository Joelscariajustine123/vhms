from django.urls import path
from . import views

app_name = 'blockchain'

urlpatterns = [
     path('add_record/', views.add_medical_record, name='add_record'),
     path('validate_chain/', views.validate_chain, name='validate_chain'),
     path('get_blockchain/', views.get_blockchain, name='get_blockchain'),
]







