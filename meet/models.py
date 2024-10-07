from django.db import models

class DateTable(models.Model):
    name= models.CharField(max_length=200,null=True,blank=True)
    agreed = models.BooleanField(default=False)
    date=models.DateField(null=True,blank=True)
    time=models.TimeField(null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return f'Date: {str(self.date)} and Time: {str(self.time)}'
    