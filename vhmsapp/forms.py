from django import forms
from django.contrib.auth.models import User
from .models import Animal, Medicine, Admission, AnimalTreatment

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'species', 'breed', 'owner', 'colour', 'age', 'gender', 'image', 'note']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['medicinename', 'make', 'cost_price', 'sale_price', 'quantity_in_stock',
        'contains', 'therapy', 'sideeffects']

class AdmdissionForm(forms.ModelForm):
    class Meta:
        model=Admission
        fields=['admissiondate', 'dischargedate', 'animal', 'admitedby']

class AnimalTreatmentForm(forms.ModelForm):
    class Meta:
        model=AnimalTreatment
        fields=['admission', 'doctor', 'medicine', 'quantity', 'treatmentdate', 'doctorfee', 
        'nursingfee', 'hospitalfee', 'note']
     # id, 
