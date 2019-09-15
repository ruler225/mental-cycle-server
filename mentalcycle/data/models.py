from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RatingManager(models.Manager):
    def getRatingsForUser(self, desiredUser):
        ratings = self.filter(user=desiredUser)
        return ratings
    


class DayRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True)
    rating = models.IntegerField()
    description = models.TextField()

    objects = RatingManager()




