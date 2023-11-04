from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
def file_upload(instance, filename):
    if filename:
        image_name, extension = filename.split('.')
        return f"jobs/{instance.id}/{instance.id}.{extension}"
    return instance

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
    pic = models.ImageField(upload_to=file_upload, blank=True)
    slug = models.SlugField(null=True,blank=True)
    def save(self, *arg, **kwargs):
        # logic
        self.slug = slugify(self.title)
        super(Job,self).save(*arg, **kwargs)

    def __str__(self) :
        return f"[{self.title}]"
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) :
        return f"[{self.name}]"
    
