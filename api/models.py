from django.db import models

# Create your models here.
class couple(models.Model):
    male = models.CharField(max_length=30)
    female = models.CharField(max_length=30)
    relationship_status = models.CharField(max_length=20)
    common_interest = models.TextField()
    fav_spots = models.TextField()

    def __str__(self):
        return self.relationship_status 