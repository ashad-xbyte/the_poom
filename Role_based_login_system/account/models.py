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