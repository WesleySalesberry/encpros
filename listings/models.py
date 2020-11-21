from django.db import models
from django.utils import timezone
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(max_length=200, blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photos_main = models.ImageField(upload_to='photos/main')
    #photos = models.ImageField(blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title


class ListingPhoto(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='photos/main/inside')

    def __str__(self):
        return self.title
