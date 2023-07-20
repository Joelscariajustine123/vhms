from django.contrib import admin
from .models import MedicinePurchase,Bill,Admission,Appointment,BillEntry,Employee
from .models import Person,Animal,Doctor,Medicine,AnimalTreatment,Hospital,DoctorAppointment,Department
# Register your models here.
admin.site.register(Person)
admin.site.register(Animal)
admin.site.register(Doctor)
admin.site.register(Medicine)
admin.site.register(AnimalTreatment)
admin.site.register(MedicinePurchase)
admin.site.register(Admission)
admin.site.register(Bill)
admin.site.register(Appointment)
admin.site.register(BillEntry)
admin.site.register(Employee)
admin.site.register(DoctorAppointment)
admin.site.register(Hospital)
admin.site.register(Department)