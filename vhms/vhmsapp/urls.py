from django.urls import path
from vhmsapp import views
from .views import user_profile,hospital_list,bill_page,login_error
from .views import animal_dashboard
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home', views.home, name='home'),
    path('login_r/', views.login_r, name='login required'),
    path('sign_up/', views.sign_up, name='signin'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),

    path('hospitals/', views.hospital_list_view, name='Direction'),
    path('Contact/', views.search_contact, name='Contact'),
    path('doctors/', views.doctors_list, name='FindDoc'),
    path('MedInfo/', views.MedInfo, name='MedInfo'),
    path('medicines/', views.medicines ,name="Medicines Grid"),
    path('new_medicine/', views.new_medicine ,name="Create Medicine Record"),


    path('menu_doctor/', views.menu_doctor, name='menu_doctor'),
    path('menu_animal_owner/', views.menu_animal_owner, name='menu_animal_owner'),
    path('menu_regular/', views.menu_regular, name='menu_regular'),
    path('Menu', views.menu, name='Menu'),
    path('MI_p1/', views.MI_p1, name='MI_p1'),
    path('MI_p2/', views.MI_p2, name='MI_p2'),
    path('MI_p3/', views.MI_p3, name='MI_p3'),
    path('MI_p4/', views.MI_p4, name='MI_p4'),
    path('MI_p5/', views.MI_p5, name='MI_p5'),
    path('MI_p6/', views.MI_p6, name='MI_p6'),
    path('MI_p7/', views.MI_p7, name='MI_p7'),
    path('MI_p8/', views.MI_p8, name='MI_p8'),
    path('login/error/', views.login_error, name='login_error'),
    
    path('animal_dashboard/', views.animal_dashboard, name='animal_dashboard'),
    path('all_pets/', views.all_pets, name='all_pets_dashboard'),

    
    path('get_hospitals/', views.get_hospitals, name='get_hospitals'),
    path('get_departments/', views.get_departments, name='get_departments'),
    path('get_doctors/',views.get_doctors, name='get_doctors'),

    

    path('user_profile/', views.user_profile, name='pet_owner_profile'),
    path('add_pet', views.add_pet, name='add_pet'),
    path('pet_added/', views.pet_added, name='pet_added'),
    
    path('doctor_profile/<int:doctor_id>/', views.doctor_profile, name='doctor_profile'),


    

    path('admission_by_doctor_data/', views.admission_by_doctor_data, name='hospital_list'),
    path('treatement/<int:admission_id>/', views.treatement, name='Pet Treatement'),


    
    path('hospitals/', views.hospital_list, name='hospital_list'),
    path('bill/', views.bill_page, name='bill_page'),
    path('payment-processing/', views.payment_processing, name='payment_processing'),
    path('payment-success/', views.payment_success, name='payment_success'),
   
    path('patient_list', views.animals_treated_by_doctor, name='animals_treated'),
    #path('animal_medical_history/<int:animal_id>/', views.animal_medical_history, name='animal_medical_history'),

    path('get_hospitals/', views.get_hospitals, name='get_hospitals'),
    path('get_departments/', views.get_departments, name='get_departments'),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),


    #path('make_appointment/', views.create_appointment, name='create_appointment'),


    path('pet/<int:pet_id>/', views.pet_details, name='pet_details'),

    ]




# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)