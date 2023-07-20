from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User






class VeterinaryRecord(models.Model):
    # Fields for veterinary record
    patient_name = models.CharField(max_length=100)
    patient_address = models.CharField(max_length=42)  # Ethereum address field

    # Other fields...

    # Blockchain-related fields
    transaction_hash = models.CharField(max_length=66)  # Ethereum transaction hash field
    block_number = models.PositiveIntegerField()


    

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, blank=True, verbose_name="Phone Numbers")
    email = models.EmailField(max_length=100, blank=True, verbose_name="Email Id")
    departments = models.ManyToManyField(Department, blank=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    title = models.CharField(max_length=10, default="Mr", verbose_name="Title")
    fname = models.CharField(max_length=50, default="", verbose_name="First Name")
    lname = models.CharField(max_length=50, default="", verbose_name="Last Name")
    house = models.CharField(max_length=50, blank=True, verbose_name="House Name")
    street = models.CharField(max_length=50, blank=True, verbose_name="Street")
    locality = models.CharField(max_length=50, blank=True, verbose_name="Locality")
    city = models.CharField(max_length=50, blank=True, verbose_name="City")
    state = models.CharField(max_length=50, blank=True, verbose_name="State", default="Kerala")
    pin = models.IntegerField(default=670645, verbose_name="PIN Code")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Phone Numbers")
    email = models.EmailField(max_length=100, blank=True, verbose_name="Email Id")
    birthdate = models.DateField(verbose_name="Date of Birth", blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    loginid = models.CharField(max_length=40, verbose_name="Login Id", blank=True, null=True)
    password = models.CharField(max_length=20, verbose_name="Password", blank=True, null=True)
    forget_password_hint_question = models.CharField(
        max_length=100, default="Name of the first school you studied", verbose_name="Forget Password Hint Question",
        blank=True, null=True
    )
    forget_password_hint_answer = models.CharField(
        max_length=100, default="vjec@fml", verbose_name="Forget Password Hint Answer", blank=True, null=True
    )
    address = models.CharField(max_length=30, default="Chemberi")
    zip_code = models.CharField(max_length=10, default="670764")

    def __str__(self):
        return f"{self.title} {self.fname} {self.lname}"

    class Meta:
        verbose_name_plural = "People"

    def get_full_name(self):
        return f"{self.title} {self.fname} {self.lname}"


class Animal(models.Model):
    name = models.CharField(max_length=100, default="", verbose_name="Animal Name ", blank=True, null=True)
    species = models.CharField(max_length=100, default="", verbose_name="Animal Species", blank=True, null=True)
    breed = models.CharField(max_length=100, default="", verbose_name="Animal Breed", blank=True, null=True)
    owner = models.ForeignKey(Person, verbose_name='Owner', on_delete=models.CASCADE, blank=True, null=True)
    colour = models.CharField(max_length=30, default="Black", verbose_name="Animal Colour", blank=True, null=True)
    age = models.IntegerField(default=1)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), blank=True, null=True)
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)
    note = models.CharField(max_length=225, verbose_name="Note", blank=True, default="")

    def __str__(self):
        return f"{self.name},{self.colour},{self.age},{self.gender} of {self.owner}"

    class Meta:
        verbose_name_plural = "Animals"


class Doctor(models.Model):
    person = models.OneToOneField(Person, verbose_name='Person Data', on_delete=models.CASCADE, blank=True, null=True)
    hospital = models.ForeignKey(Hospital, verbose_name='Hospital', on_delete=models.CASCADE, blank=True, null=True)
    designation = models.CharField(max_length=60, verbose_name="Designation", default="Doctor")
    joindate = models.DateField(verbose_name="Date of Join", blank=True, null=True)
    exitdate = models.DateField(verbose_name="Date of Exit", blank=True, null=True)
    qualifications = models.CharField(max_length=100, default=" DVM, DACVIM")
    experience = models.TextField()
    specialty = models.CharField(max_length=100,blank=True, null=True)
    education = models.TextField(max_length=1000,blank=True, null=True)
    departments = models.ManyToManyField(Department, blank=True)

    def __str__(self):
        return f"{self.person}, {self.designation}, {self.person.phone}, {self.person.email}"

    class Meta:
        verbose_name_plural = "Doctors"


class Medicine(models.Model):
    medicinename = models.CharField(max_length=100, verbose_name="Medicine Name", blank=True, null=True)
    cost_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Cost Price", blank=True, null=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Sale Price", blank=True, null=True)
    quantity_in_stock = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quantity in Stock", default=0)
    make = models.CharField(max_length=60, verbose_name="Manufacturing Company", blank=True, null=True)
    contains = models.CharField(max_length=100, verbose_name="Contains-(API)", blank=True, null=True)
    #API Active Pharmacuticla Ingradient
    therapy = models.CharField(max_length=100, verbose_name="Therapy or Usage", blank=True, null=True)
    sideeffects = models.CharField(max_length=100, verbose_name="Side effects if any", blank=True, null=True)

    def __str__(self):
        return f"{self.medicinename}, {self.cost_price}, {self.sale_price}, {self.quantity_in_stock}, {self.make}"

    class Meta:
        verbose_name_plural = "Medicines"


class MedicinePurchase(models.Model):
    medicine = models.ForeignKey(Medicine, verbose_name='Medicine_ID', on_delete=models.CASCADE, blank=True, null=True)
    purchasedate = models.DateField(verbose_name="Date of Purchase", default=timezone.now, blank=True, null=True)
    pquantity = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Purchasing Quantity", default=1)
    supplier = models.CharField(max_length=100, verbose_name="Supplier of the Medicine", blank=True, null=True)
    supplier_invoice_no = models.CharField(max_length=50, blank=True, verbose_name="Supplier Invoice Number")

    def __str__(self):
        return f"{self.supplier_invoice_no}, {self.medicine.medicinename}, {self.purchasedate}, {self.pquantity}"

    class Meta:
        verbose_name_plural = "Medicine Purchases"


class Employee(models.Model):
    person = models.OneToOneField(Person, verbose_name='Person Data', on_delete=models.CASCADE, blank=True, null=True)
    designation = models.CharField(max_length=60, verbose_name="Designation", default="Staff")
    joindate = models.DateField(verbose_name="Date of Join", blank=True, null=True)
    exitdate = models.DateField(verbose_name="Date of Exit", blank=True, null=True)
    department = models.CharField(max_length=100, default="Administration")
    qualifications = models.CharField(max_length=100, default="Degree in relevant field")
    experience = models.TextField()

    def __str__(self):
        return f"{self.person}, {self.designation}, {self.person.phone}, {self.person.email}"

    class Meta:
        verbose_name_plural = "Employees"


class Appointment(models.Model):
    animal = models.ForeignKey(Animal, verbose_name='Animal_ID', on_delete=models.CASCADE, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, verbose_name='Doctor_ID', on_delete=models.CASCADE, blank=True, null=True, related_name='appointments')
    appointmentdate = models.DateField(verbose_name="Appointment Date", default=timezone.now)
    starttime = models.TimeField(verbose_name="Start Time", default=timezone.now)
    endtime = models.TimeField(verbose_name="End Time", default=timezone.now)
    note = models.CharField(max_length=225, verbose_name="Note", blank=True, default="")

    def __str__(self):
        return f"{self.animal}, with: {self.doctor}, on: {self.appointmentdate}, from: {self.starttime} to: {self.endtime}"

    class Meta:
        verbose_name_plural = "Appointments"


class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    person = models.ForeignKey(Person, verbose_name='Person Data', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.user}, {self.person}"

    class Meta:
        verbose_name_plural = "User Registrations"


class Admission(models.Model):
    admissiondate = models.DateField(verbose_name="Admission Date", blank=True, default=timezone.now)
    dischargedate = models.DateField(blank=True, verbose_name="Discharge Date", default=timezone.now)
    animal = models.ForeignKey(Animal, verbose_name='Animal_ID', on_delete=models.CASCADE, 
        blank=True, null=True)
    admitedby = models.ForeignKey(Doctor, verbose_name="Dctor in charege of admission",
        on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.animal} - {self.admitedby} << {self.admissiondate},  {self.dischargedate} >>"

    class Meta:
        verbose_name_plural = "Admission"


class AnimalTreatment(models.Model):
    admission = models.ForeignKey(Admission, verbose_name="Treatment Admission Id", on_delete=models.CASCADE,
                                  blank=True, null=True)
    doctor = models.ForeignKey(Doctor, verbose_name='Treatment giving doctor', on_delete=models.CASCADE,
                               blank=True, null=True)
    medicine = models.ForeignKey(Medicine, verbose_name='Medicine_ID', on_delete=models.CASCADE,
                                 blank=True, null=True)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Quantity of Medicine",
                                   default=1, blank=True, null=True)
    treatmentdate = models.DateField(verbose_name="Date of Treatment", default=timezone.now)
    doctorfee = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Doctor's Fee",
                                    default=0, blank=True, null=True)
    nursingfee = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Nursing Fees",
                                     default=0, blank=True, null=True)
    hospitalfee = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Hospital Fees",
                                      default=0, blank=True, null=True)
    note = models.CharField(max_length=255, verbose_name="Note of Treatment", default="", null=True)
    

    def __str__(self):
        amount = self.medicine.sale_price * self.quantity + self.doctorfee + self.nursingfee + self.hospitalfee
        return f"{self.admission}, {self.admission.animal}, {self.treatmentdate}, Total Amount: {amount}"

    class Meta:
        verbose_name_plural = "Animal Treatments"


class Bill(models.Model):
    billdate = models.DateField(verbose_name="Bill Date", default=timezone.now)
    admission = models.ForeignKey(Admission, verbose_name='Animal on Treatment Admission',
                                  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.billdate} - {self.admission.animal}"

    class Meta:
        verbose_name_plural = "Bills"


class BillEntry(models.Model):
    bill = models.ForeignKey(Bill, verbose_name="Bill of the Entry", on_delete=models.CASCADE, blank=True, null=True)
    treatment = models.ForeignKey(AnimalTreatment, verbose_name='Treatment on Bill',
                                  on_delete=models.CASCADE, blank=True, null=True)
    slno = models.IntegerField(default=1, verbose_name="Serial no on bill")

    def __str__(self):
        return f"{self.bill} - {self.treatment}"

    class Meta:
        verbose_name_plural = "Bill Entries"


class Treatment(models.Model):
    name = models.CharField(max_length=100, verbose_name="Treatment Name")
    cost = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Treatment Cost")
    description = models.TextField(verbose_name="Description", blank=True)
    duration = models.DurationField(verbose_name="Duration", blank=True, null=True)
    is_available = models.BooleanField(verbose_name="Is Available", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Treatments"

class DoctorAppointment(models.Model):
    doctor = models.ForeignKey(Doctor, verbose_name='Doctor', on_delete=models.CASCADE, related_name='doctor_appointments')
    appointment = models.ForeignKey(Appointment, verbose_name='Appointment', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor} - {self.appointment}"
