from django.shortcuts import render, redirect ,get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Freelancer, Company, Job, Transaction
from django.contrib.auth.models import User 
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as loginUser,logout

def Home(request):
    return render(request, 'landing.html', {})
  
  
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'User created successfully')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
    
    return render(request, 'signup.html')

@login_required(login_url='login')
def UserDashbord(request):
    user = request.user
    freelancer= Freelancer.objects.filter(user=user).first()
    all_Freelancer= Freelancer.objects.all()
    all_Jobs=Job.objects.all()
    freelancer_already_created= False if freelancer is None else True
    return render(request,'dashboard.html', {"link":"dashboard", 'freelancer' : freelancer, 'freelancer_exist': freelancer_already_created, "freelancer": all_Freelancer, "Jobs":all_Jobs})

@login_required(login_url='login')
def userProfile(request):
 return render(request,'Mangement.html',{})

@login_required(login_url='login')
def adminDashVeiw(request):
  all_Freelancer= Freelancer.objects.all()
  all_Jobs=Job.objects.all()
  all_company=Company.objects.all()
  return render(request,"Admindashboard.html", {"freelancer": all_Freelancer, "Jobs":all_Jobs, "company" : all_company} )

@login_required(login_url='login')
def Table(request):
  all_Jobs=Job.objects.all()
  return render(request,"Opportunity.html", { "link":"Opportunity", "Jobs":all_Jobs, } )

@login_required(login_url='login')
def Registration(request):
  error=None
  if request.method == 'POST':
    firstname = request.POST['first-name']
    lastname = request.POST['last-name']
    country = request.POST['Country']
    state = request.POST['state']
    skills = request.POST['skills']
    try :
      freelancer_exist= Freelancer.objects.create(user=request.user, firstname=firstname, lastname=lastname, country=country, state=state , skills=skills )
      if freelancer_exist:
        return redirect('user-dashboard')
      else:
        error = 'Could not create Account 😫'
    except Exception as e:
      error =e
      print(e)
  return render(request, 'Freelancer.html',{'usernames': request.user.username,'error':error})
def login(request):
  errormessage=None
  if request.method =='POST':   
    username = request.POST['username'] 
    password = request.POST['password']
    user = authenticate(request,username=username ,password=password) 
  
    if user:
      loginUser(request , user)
      return redirect('user-dashboard')
    else:
      errormessage='Invalid username or password'
  return render(request, 'login.html',{"errormessage":errormessage})

@login_required(login_url='login')
def post_job(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        required_skills = request.POST.get('required_skills')
        job = Job.objects.create(
            title=title,
            description=description,
            required_skills=required_skills,
            company=company
        )
        return redirect('job_detail', job.id)
    return render(request, ' post_job.html', {'company': company})
@login_required(login_url=login)
def apply_for_job(request, freelancer_id, job_id):
    freelancer = get_object_or_404(Freelancer, id=freelancer_id)
    job = get_object_or_404(Job, id=job_id)
    if job.is_open:
        # Logic for applying to the job (add the freelancer to job's application list)
        job.is_open = False  # Close the job after application
        job.save()
        return HttpResponse(f"{freelancer.firstname} applied for job {job.title}.")
    else:
        return HttpResponse("Job is closed.")
    
@login_required(login_url=login)
def hire_freelancer(request, company_id, job_id, freelancer_id):
    company = get_object_or_404(Company, id=company_id)
    job = get_object_or_404(Job, id=job_id)
    freelancer = get_object_or_404(Freelancer, id=freelancer_id)
    if job.is_open:
        job.is_open = False
        job.save()
        transaction = Transaction.objects.create(
            company=company,
            freelancer=freelancer,
            job=job
        )
        return HttpResponse(f"Company {company.name} hired {freelancer.firstname} for job {job.title}. Transaction ID: {transaction.id}")
    return HttpResponse("Job is closed.")



