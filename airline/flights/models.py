from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Airport(models.Model):                    # if we hover over imported class the vs code shows the parameters of class and parameters type or datatype of parameters taken by class and also shows return type
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")   # ForeignKey class inherits Airport class     
    destination = models.ForeignKey(Airport, on_delete=CASCADE, related_name="arrivals")
    duration = models.IntegerField()
 
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"