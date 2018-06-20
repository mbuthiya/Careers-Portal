from django.db import models

# Create your models here.

class Location(models.Model):
    """
    Location model class that defines properties of the Location
    """

    location_name = models.CharField(max_length=80)
    country_extension = models.CharField(max_length=6)
    location_image = models.ImageField(upload_to='locations/')


    def __str__(self):
        return f"{self.location_name} Location Model"


class Job(models.Model):
    """
    Job model class that define the properties of the job offered.
    """
    job_title = models.CharField(max_length=300)
    job_description = models.TextField()
    requirements = models.TextField()
    responsibilities = models.TextField()
    characteristics = models.TextField()
    manager = models.EmailField()
    type = models.CharField(max_length=50)
    location= models.ForeignKey('Location',on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.job_title} Job Model"


class Application(models.Model):
    """
    Application model class that stores the properties of a user applicaion.
    """
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    gender=models.CharField(max_length=10)
    passport_photo = models.ImageField(upload_to='passport')
    phone_number = models.CharField(max_length=10)
    programming_languages=models.TextField()
    curriculum_vitae = models.URLField()
    cover_letter = models.URLField()
    job = models.ForeignKey('Job',on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.firstname} Application model"
