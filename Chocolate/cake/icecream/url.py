from django.urls import path, include
from .import views 

urlpatterns =[
  path('', views.Home, name='Home'),
  path('Opportunity/', views.Table, name='Opportunity' ),
  path('Freelancer/', views.adminDashVeiw, name='freelancer-admin-home'),
  path('Register', views.Registration, name = 'register'),
  path('profile/',views.userProfile,name='profile'),
  path('dashboard/', views.UserDashbord, name='user-dashboard'),
  path('signup/', views.signup, name='signup' ),
  path('post-job/<uuid:company_id>/', views.post_job, name='post_job'),
  path('login/', views.login, name= 'login'),
  path('apply-job/<uuid:freelancer_id>/<uuid:job_id>/', views.apply_for_job, name='apply_for_job'),
  path('hire-freelancer/<uuid:company_id>/<uuid:job_id>/<uuid:freelancer_id>/', views.hire_freelancer, name='hire_freelancer'),
]