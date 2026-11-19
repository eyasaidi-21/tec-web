from django.db import models
from AccountApp.models import Doctor, patient

# Create your models here.
class Appointment(models.Model):
    reason = models.TextField(max_length=100)
    prescription = models.FileField(
        blank=True,
        upload_to='prescriptions/',
    )
    class status(models.TextField):
        PENDING = "PENDING","En attente"
        ACCEPTED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'
    status = models.CharField(max_length=10, choices=status.choices, default=status.PENDING)
    duration_minutes = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_date = models.DateTimeField()
    doctor = models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey('AccountApp.patient', on_delete=models.CASCADE, related_name='appointments')
    




apps.py


from django.apps import AppConfig


class AppointmentappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AppointmentApp'
