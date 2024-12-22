from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import cofee, Register
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

#About page:
def about(request):
    return render(request, 'front.html')
def aboutus(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def location(request):
    return render (request,'location.html')


#login_view function:
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

#home function

def home(request):
    cofee1 = cofee.objects.all()
    print(cofee1)
    return render(request, 'home.html', {'cofee': cofee1})


#order function
def order(request):
    if request.method == "POST":
        print('p0st request called')
        
        name = request.POST.get ('name')
        price = request.POST.get ('price')
        image = request.POST.get('image')
        quantity = request.POST.get('quantity') 
        
        print(f"name{name},price{price},quatity{quantity},image{image}")
        total_cost = 20
        
        return render(request, 'result.html', {
            'name': name, 
            'price': price, 
            'image':image,
           
            'total_cost': total_cost
        })
    return render(request, 'index.html')

#Register Function:
def Registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email_id = request.POST.get('email_id') 
        password = request.POST.get('password')
        conf_pass = request.POST.get('conf_pass')
        

        # Check if email is valid
        if not email_id.endswith('@gmail.com'):
            messages.warning(request, 'Please enter a valid Gmail address')
            return render(request, 'Register.html')

         # Check if password is valid
        if password == conf_pass:
            
            try:
                user = User.objects.create_user(username=username, email=email_id, password=password)
                user.save()
                
                Register.objects.create(Username=username, Email_id=email_id, Password=password)
                messages.success(request, 'You are registered successfully')
                return redirect('login')
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
                return render(request, 'login.html')

        else:
            messages.warning(request, 'Password and Confirm Password should match.')
            return render(request, 'Register.html')

    return render(request, 'Register.html')

#end:
from django.shortcuts import render

def end(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        print(f"Name: {name}, Price: {price}, Quantity: {quantity}")
        try:
            price = float(price) 
            quantity = int(quantity)  
        except ValueError:
            return render(request, 'index.html'), {
                'error': 'Invalid input! Ensure price is a number and quantity is an integer.',
            }
                          
        total = price * quantity
        print(f"Name: {name}, Price: {price}, Quantity: {quantity}, Total: {total}")

        return render(request, 'index.html', {
            'name': name,
            'price': price,
            'quantity': quantity,
            'total': total,
        })
        
    return render(request, 'index.html')
