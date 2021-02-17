from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.TextField()
    company_name = forms.CharField(max_length=30)
    operation_countries = forms.CharField(max_length=40)
    objective = forms.CharField(max_length=40)
    more_details_description = modformsels.TextField()

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'phone', 'company_name', 'objective', 'more_details_description']
