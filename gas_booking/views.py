from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from pathlib import Path
from .forms import Sign_up,Login,Service_Requests
from .models import User,Services

def home(request):
    formS = Sign_up()
    formL = Login()
    if request.method == "POST" and "username" not in request.session:
        if request.POST.get("form_type")=="sign_in":
            formS = Sign_up(request.POST)
            if formS.is_valid():
            
                form_data = formS.cleaned_data.get("username")
                if User.objects.filter(username=form_data).exists():
                    messages.error(request, "This username is already. Please enter a new username")
                else:
                    formS.save()
                    messages.success(request, "Account created successfully please login")
                    return redirect('home')
            else:
                messages.error(request,"Invlaid data entered")
                return redirect('home')
        else:
            formL = Login(request.POST)
            if formL.is_valid():
                username = formL.cleaned_data.get("username")
                password = formL.cleaned_data.get("password")
                
                if username == "supporter" and password == "1234":
                    return redirect('handle_requests')
                
                if User.objects.filter(username=username).exists():
                    if User.objects.filter(password=password).exists():
                        request.session["username"] = username
                        request.session["password"] = password
                        messages.success(request, "Logged in successfully")
                        
                        return redirect('home')
                    else:
                        messages.error(request,"Incorrect password entered")
                        return redirect('home')
                else:
                    messages.error(request, "No account found with this username")
                    return redirect('home')
            else:
                messages.error("Invalid login data. Check the fields you entered.")
                return redirect('home')
    elif request.method=="POST" and "username" in request.session:
        messages.error(request,"Already logged in")
        return redirect('home')
    else:
        return render(request,'home.html',{'formS': formS,'formL':formL})
    
def service_requests(request):
    if "username" in request.session:
        if request.method == "POST":
            form = Service_Requests(request.POST, request.FILES)
            if form.is_valid():
                service_request=form.save(commit=False)
                service_request.username = request.session["username"]
                service_request.save()
                messages.success(request,"Request submitted successfully")
                return redirect('home')  
        else:
            form = Service_Requests()
            return render(request, 'service_request.html', {'form': form})
    else:
        messages.error(request,"You need to login to use this feature ")
        return redirect('home')

def logout_view(request):
    request.session.flush()
    messages.success(request,"Logout successfull")
    return redirect('home')

def track_requests(request):
    if "username" not in request.session:
        messages.error(request,"You need to login to use this feature")
        return redirect('home')
    else:
        username = request.session["username"]
        submitted_requests = Services.objects.filter(username=username)
        return render(request,"submitted_requests.html",{'requests': submitted_requests})
        
from django.shortcuts import render
from .models import Services, User

def handle_requests(request):
    service_requests = Services.objects.all()
    
    usernames = [requests.username for requests in service_requests]
    
    user_phone_numbers = []
    
    for username in usernames:
        user = User.objects.filter(username=username).first()
        if user:
            user_phone_numbers.append(user.phone)
        else:
            user_phone_numbers.append(None)  
    
    zipped_requests = zip(service_requests, user_phone_numbers)
    
    zipped_requests_list = list(zipped_requests)
    
    return render(request, 'supporters.html', {
        'zipped_requests': zipped_requests_list,
    })
