import os

from django.http import HttpResponse, JsonResponse

from django.contrib.auth.models import User
from django.db.models import Q

from django.shortcuts import render, get_object_or_404, redirect

from .models import Person, Animal, Doctor,Treatment,AnimalTreatment,Medicine, Hospital, Department

from .models import DoctorAppointment, Appointment,Department, Admission
from .forms import AnimalForm, MedicineForm
from django.contrib.auth.decorators import login_required
# from django.shortcfrom django.shortcuts import render, get_object_or_404
# from .models import Animal

# Create your views here.

# from blockchain.web3_utils import web3

def my_view(request):
    # Retrieve blockchain data
    latest_block = web3.eth.getBlock('latest')
    transaction_count = web3.eth.getTransactionCount('0x123456789...')

    # Send transaction
    tx_hash = web3.eth.sendTransaction({
        'from': '0x123456789...',
        'to': '0x987654321...',
        'value': web3.toWei(1, 'ether')
    })


def home(request):
    return render(request, 'home.html', {})

def MedInfo(request):
    return render(request, 'MedInfo.html', {})

def MI_p1(request):
    return render(request, 'MI_p1.html')

def MI_p2(request):
    return render(request, 'MI_p2.html')

def MI_p3(request):
    return render(request, 'MI_p3.html')

def MI_p4(request):
    return render(request, 'MI_p4.html')

def MI_p5(request):
    return render(request, 'MI_p5.html')

def MI_p6(request):
    return render(request, 'MI_p6.html')

def MI_p7(request):
    return render(request, 'MI_p7.html')

def MI_p8(request):
    return render(request, 'MI_p8.html')

def login_r(request):
    return render(request, 'login.html')



def menu_doctor(request):
    return render(request, 'menu_doctor.html')


def menu_animal_owner(request):
    return render(request, 'menu_animal_owner.html')

def menu_regular(request):
    return render(request, 'menu_regular.html')


def menu(request):
    return render(request, 'Menu.html')

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'FindDoc.html', {'doctors': doctors})

def sign_up(request):
    if request.method == "GET":
        return render(request, 'Signin.html')
    elif request.method == "POST":
        person = Person()
        person.fname = request.POST["fname"]
        person.lname = request.POST["lname"]
        person.title = request.POST["ddtitle"]
        person.house = request.POST["house"]
        person.street = request.POST["street"]
        person.locality = request.POST["locality"]
        person.city = request.POST["city"]
        person.pin = request.POST["pin"]
        person.email = request.POST["email"]
        person.phone = request.POST["phone"]
        person.loginid = request.POST["loginid"]
        person.password = request.POST["password"]
        person.forget_password_hint_question = request.POST["ddpasswordhintq"]
        person.forget_password_hint_answer = request.POST["passworha"]
        person.state = request.POST["state"]
        person.save()
        
        # Redirect to pet owner profile
        request.session["loginid"] = person.loginid
        request.session["pid"] = person.id
        request.session["pname"] = person.get_full_name()
        return redirect('/vhms/user_profile/')
    else:
        pass



def user_profile(request):
    # Retrieve the necessary details from the session
    pid = request.session.get('pid')
    pname = request.session.get('pname')
    
    # Retrieve the email and phone number from the database using the Person model
    person = Person.objects.get(id=pid)
    doc = Doctor.objects.filter(person=person).first()
    
    # Render the profile page with the retrieved details and pet information
    context_data={'person':person}
    if doc:
        context_data['doctor']=doc
    return render(request, 'user_profile.html', context_data)
      

def login_view(request):
    print("login")
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        prsn = Person.objects.filter(Q(loginid=un) & Q(password=pw)).first()
        doc = Doctor.objects.filter(person=prsn).first()
        if prsn:
            request.session["loginid"] = un
            request.session["pid"] = prsn.id
            request.session["pname"] = f"{prsn.title} {prsn.fname} {prsn.lname}"
            for key, val in request.session.items():
                print(key, val)
            # print(request.session)
            if doc:
                request.session["usertype"]="doctor"
                # return redirect('doctor_profile', doctor_id=doc.id)  # Update the redirect URL
            else:
                request.session["usertype"]="pet_owner"
                # return redirect('pet_owner_profile')
            return redirect('home')
        else:
            return redirect('/vhms/error/')
    else:
        pass



# from django.contrib.auth import logout
def logout(request):
    # Session.objects.all().delete()
    # print("-cleared-"*3)  
    request.session.flush()
    return redirect('home')


def login_error(request):
    return render(request, 'login_error.html')



def search_contact(request):
    if request.method == 'GET':
        hospital_name = request.GET.get('hospital_name')
        if hospital_name:
            hospitals = Hospital.objects.filter(name__icontains=hospital_name)
            if hospitals:
                context = {
                    'hospitals': hospitals
                }
                return render(request, 'Contact.html', context)
            else:
                context = {
                    'error_message': 'Hospital not found'
                }
                return render(request, 'contact_us.html', context)
        else:
            context = {
                'error_message': 'Please enter a hospital name'
            }
            return render(request, 'Contact.html', context)

def search(request):
    query = request.GET.get('query')
    hospitals = Hospital.objects.filter(departments__icontains=query)
    doctors = Doctor.objects.filter(name__icontains=query)
    
    context = {
        'hospitals': hospitals,
        'doctors': doctors,
        'query': query
    }
    return render(request, 'search.html', context)

def hospital_list_view(request):
    hospitals = Hospital.objects.all()
    context = {
        'hospitals': hospitals
    }
    return render(request, 'hospital_list.html', context)

def medicines(request):
    medicines=Medicine.objects.all()
    context={'medicines':medicines, }
    return render(request, 'medicines.html', context)


def doctor_profile(request, doctor_id):
    # Retrieve the doctor object based on the provided doctor_id
    doctor = get_object_or_404(Doctor, id=doctor_id)
    
    # Render the doctor profile page with the retrieved doctor object
    return render(request, 'doctor_profile.html', {'doctor': doctor})


# def add_pet(request):
#     if request.method == 'POST':
#         animalname = request.POST['animalname']
#         species = request.POST['species']
#         breed = request.POST['breed']
#         colour = request.POST['colour']
#         age = request.POST['age']
#         gender = request.POST['gender']
#         note = request.POST['note']

#         # Retrieve the logged-in user's ID from the session
#         user_id = request.session.get('pid')

#         try:
#             # Retrieve the Person instance based on the user ID
#             person = Person.objects.get(id=user_id)

#             # Create a new Animal object and associate it with the owner
#             animal = Animal(
#                 name=animalname, species=species, breed=breed, colour=colour,
#                 age=age, gender=gender, note=note, owner=person
#             )

#             image_file = request.FILES.get('image')
#             if image_file:
#                 # Assign the uploaded file to the 'profile_image' field
#                 animal.profile_image = image_file

#             animal.save()

#             return redirect('pet_added')  # Redirect to a success page
#         except Person.DoesNotExist:
#             # Handle the case when the Person instance does not exist
#             return redirect('/admin/')  # Redirect to an appropriate error page or handle it as needed
#     else:
#         return render(request, 'AddPet.html')

def add_pet(request):
    if request.method=="POST":
        form = AnimalForm(request.POST, request.FILES)
        if  form.is_valid():
            form.save()
            return redirect("/vhms/animal_dashboard/")
    else:
        form=AnimalForm()
        # print(*form.fields, "\n", *form.model)
        form.bread="Kangaru"
        return render(request, 'AddPet.html', {'pet':form})
   
def new_medicine(request):
    if request.method=="POST":
        form = MedicineForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect("/vhms/medicines/")
    else:
        form=MedicineForm()
        return render(request, 'MedicineForm.html', {'form': form})

def admission_by_doctor_data(request):
    from .forms import AdmdissionForm
    if request.method=="POST":
        form = AdmdissionForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect("/vhms/admission_by_doctor_data/")
    else:
        form=AdmdissionForm()
        animals=Animal.objects.order_by('name')
        doctors=Doctor.objects.order_by('person')
        admissions=Admission.objects.order_by('animal')
        print(*admissions)
        return render(request, 'AdmissionForm.html', 
            {'dataform': form, 'pets':animals, 'doctors':doctors, 'admissions':admissions})

def pet_added(request):
    return render(request, 'pet_added.html')



def animals_treated_by_doctor(request):
    animal = Animal.objects.filter(treatment__is_available=True)
    return render(request, 'patient_list.html', {'animal': animal})


def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital_list.html', {'hospitals': hospitals})





def bill_page(request):
    # Retrieve treatment and medicine data from the database
    treatments = Treatment.objects.all()
    medicines = Medicine.objects.all()

    # Calculate the total bill
    total_bill = calculate_total_bill(treatments, medicines)  # Implement this function based on your database structure and calculation logic

    return render(request, 'bill.html', {'treatments': treatments, 'medicines': medicines, 'total_bill': total_bill})

def payment_processing(request):
    if request.method == 'POST':
        # Process the payment
        total_bill = request.POST.get('total_bill')

        # Perform the necessary payment processing logic
        # ...

        # Redirect to a success page or perform any other desired actions
        return redirect('payment_success')

    # Redirect to the bill page if the request is not a POST request
    return redirect('bill_page')



def calculate_total_bill(treatments, medicines):
    total = 0

    # Calculate the total cost of treatments
    for treatment in treatments:
        total += treatment.cost

    # Calculate the total cost of medicines
    for medicine in medicines:
        total += medicine.cost_price

    return total


def payment_success(request):
    return render(request, 'payment_success.html')


def animal_dashboard(request):
    # Retrieve the logged-in user's ID from the session
    pid = request.session['pid']
    print(pid)
    # Retrieve the animals owned by the user
    animals = Animal.objects.filter(owner__id=pid)
    return render(request, 'pet_list.html', {'animals': animals, 'title':'My Pets'})

def all_pets(request):
    # Retrieve the logged-in user's ID from the session
    if request.session['usertype']=="doctor":
        animals = Animal.objects.all()
        return render(request, 'pet_list.html', {'animals': animals, 'title': 'All Pets'})
    else:
        pid = request.session['pid']
        animals = Animal.objects.filter(owner__id=pid)
        return render(request, 'pet_list.html', {'animals': animals, 'title':'My Pets' })


@login_required
def doctor_appointments(request):
    # Retrieve the doctor associated with the authenticated user
    try:
        doctor =Person.doctor.objects.get(person=request.user)
    except Doctor.DoesNotExist:
        # Handle the case when the authenticated user is not a doctor
        doctor = None

    if doctor:
        # Retrieve the doctor's appointments
        doctor_appointments = Appointment.objects.filter(doctor=doctor)
    else:
        # If the authenticated user is not a doctor, handle it accordingly
        doctor_appointments = []

    context = {
        'doctor_appointments': doctor_appointments
    }

    return render(request, 'doctor_appointments.html', context)



def get_hospitals(request):
    hospitals = Hospital.objects.all()
    data = [{'id': hospital.id, 'name': hospital.name} for hospital in hospitals]
    return JsonResponse(data, safe=False)

def get_departments(request):
    hospital_id = request.GET.get('hospital_id')
    departments = Department.objects.filter(hospital_id=hospital_id)
    data = [{'id': department.id, 'name': department.name} for department in departments]
    return JsonResponse(data, safe=False)

def get_doctors(request):
    department_id = request.GET.get('department_id')
    doctors = Doctor.objects.filter(department_id=department_id)
    data = [{'id': doctor.id, 'name': doctor.name} for doctor in doctors]
    return JsonResponse(data, safe=False)

def make_appointment(request):
    if request.method == 'POST':
        # Handle the appointment booking logic here
        # ...
        return render(request, 'success-page.html')  # Replace 'success-page.html' with the actual success page template
    return render(request, 'Appoint.html')  # Replace 'Appoint.html' with the actual template name






def pet_details(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    return render(request, 'med_history.html', {'animals': animal})


def treatement(request, admission_id):
    from .forms import AnimalTreatmentForm
    if request.method=="POST":
        form = AnimalTreatmentForm(request.POST)
        if  form.is_valid():
            form.save()
            return redirect(f"/vhms/treatement/{admission_id}/")
    else:
        form=AnimalTreatmentForm()
        animals=Animal.objects.order_by('name')
        doctors=Doctor.objects.order_by('person')
        admissions=Admission.objects.order_by('animal')
        treatments=Treatment.objects.order_by('name')
        medicines=Medicine.objects.all()
        admission=Admission.objects.get(id=admission_id)
        # print(*admissions)
        print("---", admission, sep="\n")
        return render(request, 'AnimalTreatmentForm.html', 
            {'dataform': form, 'pets':animals, 'doctors':doctors, 'admissions':admissions,
            'medicines':medicines, 'admission':admission, 'treatments':treatments})