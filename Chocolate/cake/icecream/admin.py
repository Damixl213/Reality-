from django.contrib import admin
from.models import Freelancer, Company, Job
from.models import Transaction

# Register your models here.
admin.site.register(Freelancer)
admin.site.register(Transaction)
admin.site.register(Company)
admin.site.register(Job)