from django.db import models


class Location(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    listing_url = models.URLField()
    name = models.CharField(max_length=100)
    host_url = models.URLField
    host_name = models.CharField(max_length=100)
    precinct = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=5)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    price = models.CharField(max_length=100)#FloatField
    review_scores_rating = models.CharField(max_length=100)#IntegerField
    price_as_dp = models.CharField(max_length=100)#FloatField
    rating_as_int = models.CharField(max_length=100)#IntegerField
    precint = models.CharField(max_length=100)
    crime_count = models.CharField(max_length=100)#IntegerField
    precint_crime_rating = models.CharField(max_length=100)#FloatField
    goal_function = models.CharField(max_length=100)#FloatField
    
    def __str__(self):
        if self.name is not None and self.host_name is not None:
            return self.name + ", " + self.host_name
        else:
            return "could not return full name, sth was empty"
        
    def safety_mark(self):
        return self.goal_function