from django import forms

class upload(forms.form):
    name=forms.CharField(label="Enter Name", max_length=50)
    email=forms.EmailField()
    file=forms.FileField()