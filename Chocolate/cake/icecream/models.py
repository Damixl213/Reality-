from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from icecream.generator import generateAccountNumber
from icecream.IDcreator import IDNumber


class Freelancer(models.Model):
    id = models.CharField(max_length=8, primary_key=True, default=IDNumber, editable=False )
    user= models.OneToOneField(to=User, on_delete= models.CASCADE)
    firstname=models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    account_number=models.CharField(max_length=12, default=generateAccountNumber,unique=True)
    balance = models.DecimalField(max_digits=1000000000000000,decimal_places=2,default=0)
    skills = models.TextField(help_text="list of skills")
    country =models.CharField(max_length=100)
    state =models.TextField(max_length=155)
    
    def __str__(self):
        return self.firstname + " " + self.lastname

class Company(models.Model):
    id = models.CharField(max_length=8, primary_key=True, default=IDNumber, editable=False, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    required_skills =models.JSONField(default=dict, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_open = models.BooleanField(default=True)
    posted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Salary agreed for the job
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)  # Default interest rate set to 10%
    profit_margin = models.DecimalField(max_digits=5, decimal_places=2, default=0)  # Profit margin as a percentage

    def calculate_salary(self):
        return self.base_salary

    def calculate_interest(self):
        # Assuming interest is calculated on the base salary
        interest = (self.base_salary * self.interest_rate) / 100
        return interest

    def calculate_profit(self):
        # Assuming profit is calculated as a percentage of the base salary
        profit = (self.base_salary * self.profit_margin) / 100
        return profit

    def __str__(self):
        return f"Transaction {self.id} - {self.freelancer.firstname} hired by {self.company.name} for {self.job.title}"

    def get_financial_summary(self):
        return {
            "base_salary": self.calculate_salary(),
            "interest": self.calculate_interest(),
            "profit": self.calculate_profit(),
            "total_salary_with_interest": self.calculate_salary() + self.calculate_interest(),
        }