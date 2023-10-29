from django.db import models
from django.utils import timezone
# Create your models here.
class Job(models.Model):
    class JobType(models.TextChoices):
        FULL_TIME = 'FT','Full time'
        PARTY_TIME = 'PT', 'Party time'
    title = models.CharField(max_length=200)
    #location
    job_type = models.CharField(max_length=2,choices=JobType.choices, default=JobType.PARTY_TIME)
    description = models.TextField()  
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='jobs/')

    def __str__(self) :
        return f"[{self.title}]"
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) :
        return f"[{self.name}]"
    
