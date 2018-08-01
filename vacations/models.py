from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.validators import MaxValueValidator, MinValueValidator

@python_2_unicode_compatible
class Vacation(models.Model):

    location = models.CharField(blank=False, max_length=255)
    month = models.SmallIntegerField(blank=False, validators=[MaxValueValidator(12, "Must be number between 1 and 12"), MinValueValidator(1,"Must be a number between 1 and 12")])
    year = models.CharField(blank=False, max_length=4)
    albums = models.ManyToManyField(Album)

    def __str__(self):
        return self.location
    
    class Meta:
        db_table = 'vacations'

class Album(models.Model):

    title = models.CharField(max_length=255, blank=False)
    date_added = models.DateTimeField(auto_date_add_now=True)
    slug = models.SlugField(unique=True, max_length=250)
    description = models.TextField(blank=True)\
    is_public = models.BooleanField(default=False)
    # photos = 
    
    

    def __str__(self):
        return self.album_name
    
    class Meta:
        db_table='albums'

class Image(models.Model):

    caption = models.CharField(max_length=500, blank=True)
    album = models.ForeignKey(Album)
    picture = models.ImageField(default = 'default.png')

    def __str__(self):
        return self.caption

    class Meta: 
        db_table='images'
    
