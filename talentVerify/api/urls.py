from django.urls import path
from .import views

urlpatterns=[
    path("api/user/Company",views.CompanyView.as_view(), name="Company"),
    path("api/user/Personal_Details",views.Personal_DetailsView.as_view(), name="Personal_Details"),
    path("api/user/Employee_Details",Employee_DetailsView.as_view(), name="Employee_Details"),
]