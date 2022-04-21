from django.db import models
from django.utils.translation import gettext_lazy as _ 
# Create your models here.


class Profile(models.Model):
    full_name = models.CharField(_('full name'), max_length=100, blank=True)

    email = models.EmailField(_('email address'), max_length=255, unique=True)

    date_of_birth = models.DateField(null=True, blank=True)

    Contact_No = models.CharField(_('Contact'),max_length=17, unique=True, null=False, blank=False)

    profile_pic = models.ImageField(upload_to="media/profiles")  
    
    def __str__(self):  
        return self.full_name