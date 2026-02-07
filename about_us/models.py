from django.db import models

# Create your models here.
class About(models.Model):
    about_heading = models.CharField(max_length=200)
    about_description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.about_heading
    

class SocialLink(models.Model):
    plateform = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plateform
    
    