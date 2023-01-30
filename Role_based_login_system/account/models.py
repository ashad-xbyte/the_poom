from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_sales = models.BooleanField('Is sales', default=False)
    is_production = models.BooleanField('Is production', default=False)
    is_devloper = models.BooleanField('Is devloper', default=False)
    is_client = models.BooleanField('Is client', default=False)
    role = (('admin', "Admin"),
            ('sales', "Sales"),
            ('production', "Production"),
            ('devloper', "Developer"),
            ('client', "Client"))
    roles = models.CharField(max_length=10, choices=role, default="client")

class File_1(models.Model):
    file = models.FileField(upload_to='files', null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    is_admin_file = models.BooleanField('Is admin file', default=True)
    is_sales_file = models.BooleanField('Is sales file', default=False)
    is_production_file = models.BooleanField('Is production file', default=False)
    is_devloper_file = models.BooleanField('Is devloper file', default=False)
    is_client_file = models.BooleanField('Is client file', default=False)

    def __str__(self):
        return self.title + ": " + str(self.file)
