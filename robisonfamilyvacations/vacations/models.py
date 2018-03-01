from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator

@python_2_unicode_compatible
class vacation(models.Model):

    location = models.CharField(blank=False, max_length=255)
    month = models.SmallIntegerField(blank=False, validators=[MaxValueValidator(12, "Must be number between 1 and 12"), MinValueValidator(1,"Must be a number between 1 and 12")])
    year = models.CharField(blank=False, max_length=4)

    def __str__(self):
        return self.location
    
    
