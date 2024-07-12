from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Company,Personal_Details, Employee_Details

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwags = {"password": {"write_only": True}} 
        
    def create(self, validated_data):
        print(validated_data)
        user= User.objects.create_user(**validated_data)
        return user       
        
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=["company_name","date_of_registration","company_registration_number","address","contact_person",
                "list_of_departments","number_of_employees=models","author"]
        extra_kwags={"author":{"read_only":True}}
        
class Personal_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personal_Details
        fields=["name_of_employee","contact_phone","email_address","author"]
        extra_kwags={"author":{"read_only":True}}
        
class Employee_DetailsSerializer(serializers.ModelSerializer):
    foreign_key= Personal_DetailsSerializer
    foreign_key= CompanySerializer
    class Meta:
        model=Employee_Details
        fields=["employee_id_number"," department","role","date_started_in_each_role","date_left_role"," duties_in_each_role","foreign_key","author"]
        extra_kwags={"author":{"read_only":True}}
        