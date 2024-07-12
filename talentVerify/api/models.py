from django.db import models
from django.contrib.auth.models import User
from .models import Note,Company,Employee_Details
# Create your models here.

#class interest(models.Model):
#    title= models.CharField(max_length=200)
 #   def _str_(self):
 #       return self.title
    
#class City(models.Model):
       # title=models.CharField(max_length=200)
       # def _str_(self):
        #    return self.title
        
#class Contact(models.Model):
 #   name=models.Charfield(max_length=200)
 #   mobile=models.Charfield(max_length=20)
 #   interests=models.ManyToManyField(interest)
 
class Note(models.Model):
     title= models.CharField(max_length=100) 
     content= models.TextField()  
     created_at= models.DateTimeField(auto_now_add=True)
     author= models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
     
     def __str__(self):
         return self.title
     
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwags = {"author": {"read_only: True"}}
        
class Company(models.Model):
    company_name=models.CharField(max_length=100)
    date_of_registration=models.DateField(100)
    company_registration_number=encrypt(models.CharField())
    address=models.CharField(200)
    contact_person=models.CharField(100)
    list_of_departments=models.CharField(100)
    number_of_employees=models.int(100)
    
    def __str__(self):
        return self.company_name
    
class Personal_Details(models.Model):
    name_of_employee=models.CharField(100)
    contact_phone=models.BigAutoField(primary_key=True)
    email_address=models.EmailField(100)
    
    def __str__(self):
        return self.name_of_employee
    
    
class Employee_Details(models.Model):
    employee_id_number=encrypt(models.CharField(100))
    department=models.CharField(100)
    role=models.CharField(100)
    date_started_in_each_role=models.DateField(100)
    date_left_role=models.DateField(100)
    duties_in_each_role=models.TextField()
    foreign_key= models.ForeignKey(Personal_Details, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.department
    
    
    
    
    