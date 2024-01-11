from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from book.models import Faculty, Copy
import secrets



GENDER = [
    ('M', _('Male')),
    ('F', _('Female')),
]  

   
class Cities(models.Model):
    city = models.CharField(max_length=80)
    city_person = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.city} - {self.city_person} "
    
    class Meta:
        verbose_name = _("Cities")
        verbose_name_plural = _("Cities")


class Semesters(models.Model):
    semester = models.CharField(max_length=30)
    semester_person=models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.semester} - {self.semester_person} "
    
    class Meta:
        verbose_name = _("Semester")
        verbose_name_plural = _("Semesters")

class Desposites(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    copy= models.ForeignKey(Copy, on_delete=models.CASCADE) 
    issue_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    def __str__(self):
        return f"{self.user} - {self.copy} - {self.issue_date}"

    class Meta:
        verbose_name = "Deposit"
        verbose_name_plural = "Deposits"

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    semester = models.ForeignKey(Semesters, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=1, choices=GENDER)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
   
  
class Profile(models.Model): 
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  

    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    
    contact_no = models.CharField(max_length=14, blank=True, null=True)
    identification_no = models.CharField(max_length=10, blank=True)
    registration_no = models.CharField(max_length=10, blank=True)
    page_no = models.IntegerField(blank=True, null=True)
    original_address = models.CharField(max_length=50, blank=True, null=True)
    current_address = models.CharField(max_length=50, blank=True, null=True)
    signature = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if not (self.identification_no and self.registration_no):
            self.identification_no = secrets.token_urlsafe(3).upper().replace('_', '')[:10]
            self.registration_no = int(secrets.token_urlsafe(3), 36)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
