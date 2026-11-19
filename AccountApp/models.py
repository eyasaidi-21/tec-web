from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinimumLengthValidator , MaxlengthValidator



# Create your models here.
class User(AbstractUser):
    user_id = modeels.CharField(primary_key=True)
    pass
class Docter(User):
    license_number = models.CharField(max_length=6, unique=True  validators=[MinimumLengthValidator(6)  MaxlengthValidator(6)])
    phone = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    speciality = models.ManyToManyField('speciality' , related_name='doctors')

number_validator = RegexValidator(
    regex=r'^\d{8}$',
    message="Number must be 8 digits "
    )
def validate_birth_date(value):
    if value > timezone.locatedate():
        raise ValidationError('Birth date cannot be in the future')
class patient(user):
    national_id = models.CharField(max_length=8, unique=True  validators=[MinimumLengthValidator(8)  MaxlengthValidator(8)])
    phone = models.CharField(max_length=8 , validators =number_validator)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class speciality(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
