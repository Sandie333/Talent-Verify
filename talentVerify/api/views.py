from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewssets
from api.models import Company,Personal_Details,Employee_Details
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from api.forms import upload
from api.functions.functions import handle_uploaded_file


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class= NoteSerializer
    permission_class= [IsAuthenticated]
    
    def get_queryset(self):
        user= self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
# Create your views here.

     
class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer
    permission_classes= [AllowAny]
    
    
    
class CompanyViewSet(viewset.ModelViewsSet):
     queryset= Company.objects.all()
     serializer_class= CompanySerializer
     permission_classes=[IsAuhenticated]

     def get_queryset(self):
      user=self.request.user
      return Company.objects.filter(company_name)
    
    
class Personal_DetailsViewSet(viewset.ModelViewsSet):
    queryset= Company.objects.all()
    serializer_class= Personal_DetailsSerializer
    
    def get_queryset(self):
     user= self.request.user
     return Personal_Details.objects.filter(contact_phone)
    
    
class Employee_DetailsViewSet(viewset.ModelViewsSet):
    queryset= Company.objects.all()
    serializer_class= Employee_DetailsSerializer
    
    def get_queryset(self):
     user= self.request.user
     return Employee_Details.objects.filter(employee_id_number)
    
    
def formsubmission(request):
        form=upload()
        if request.method=="POST":
            form=upload(request.POST,request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return HttpResponse("File uploaded successfully")
            
            else:
                form=upload()
                
                
        return render(request,'api/home.html',{'form':form})
    

    
