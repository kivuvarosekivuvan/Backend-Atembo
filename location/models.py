from django.db import models


class Location(models.Model):
    region_name = models.CharField(max_length=255)
    installation_date = models.DateField(null=True, blank=True)
    updated_at = models.DateField(auto_now=True)
    

    def __str__(self):
       return self.region_name
    
  
