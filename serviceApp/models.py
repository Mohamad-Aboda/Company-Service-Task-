from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.TextField(max_length=11)
    company_name = models.CharField(max_length=30)
    operation_countries = models.CharField(max_length=40)
    objective = models.CharField(max_length=40)
    more_details_description = models.TextField()


    def __str__(self):
        return f'{self.first_name} {self.last_name}' 

