from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Userdetails
from .models import Contact
from .forms import RegisterForm

from django.contrib import messages

def home(request):
    return render(request,'homepage.html')

def booking_list(request):
    
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        city = request.POST['city'] 
        state = request.POST['state'] 
        pincode = request.POST['pincode'] 
        phonenumber = request.POST['phonenumber'] 
        emailid = request.POST['emailid'] 
        
        date = request.POST['date'] 
        time = request.POST['time'] 
        adults = request.POST['adults'] 
        kids = request.POST['kids'] 
        payment_method = request.POST['payment_method']
        specialrequest = request.POST['specialrequest']
        
        Userdetails.objects.create(
            name=name,
            address=address,
            city=city,
            state=state,
            pincode=pincode,
            phonenumber=phonenumber,
            emailid=emailid,
            date=date,
            time=time,
            adults=adults,
            kids=kids,
            payment_method=payment_method,
            specialrequest=specialrequest
        )
        return redirect('user_list')
    
    users = Userdetails.objects.all()
    return render(request, 'hotelbooking.html', {'users': users})

def view_list(request):
    
    users = Userdetails.objects.all()
    return render(request, 'view_list.html', {'users': users})

def update(request, id):
    users = get_object_or_404(Userdetails, id=id)

    if request.method == "POST":
        users.name = request.POST.get('name')
        users.address = request.POST.get('address')
        users.city = request.POST.get('city')
        users.state = request.POST.get('state')
        users.pincode = request.POST.get('pincode')
        users.phonenumber = request.POST.get('phonenumber')
        users.emailid = request.POST.get('emailid')
        users.date = request.POST.get('date')
        users.time = request.POST.get('time')
        users.adults = request.POST.get('adults')
        users.kids = request.POST.get('kids')
        users.payment_method = request.POST.get('payment_method')
        users.specialrequest = request.POST.get('specialrequest')
        users.save()

        return redirect('view_list')

    return render(request, "update.html", {'users': users})

def delete(request, id):
    user = get_object_or_404(Userdetails, id=id)

    if request.method == "POST":
        user.delete()
        return redirect('view_list')

    return render(request, 'delete.html', {'user': user})

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')

        Contact.objects.create(name=name, email=email, content=content)

        # Send email to admin
        subject = f"New Contact Message from {name}"
        message = f"Sender Name: {name}\nSender Email: {email}\n\nMessage:\n{content}"

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['manojggm14@gmail.com'],
            fail_silently=False,
        )

        # Auto-response to user
        send_mail(
            "Thank you for contacting us",
            f"Hi {name},\n\nThank you for reaching out! We have received your message and will respond shortly.\n\nBest regards,\nOur Hotel",
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        return redirect('contact')

    return render(request, "contact.html")

def login_register_page(request):
    return render(request, 'login_register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            username = User.objects.get(email=email).username
            user = authenticate(request, username=username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login_register')

    return redirect('login_register')


def register_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords don't match")
            return redirect('login_register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('login_register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('login_register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.is_staff = True
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login_register')

    return redirect('login_register')

def login_submit(request):
    return render(request,'homepage.html')