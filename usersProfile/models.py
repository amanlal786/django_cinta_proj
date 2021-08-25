from os import name
from django.db import models
from PIL import Image
from django.db.models import aggregates
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    save_name=models.BooleanField('', default=False)
    age= models.IntegerField()
    save_age=models.BooleanField('', default=False)
    skills = models.CharField(max_length=300)
    save_skills=models.BooleanField('', default=False)
    image1= models.ImageField(upload_to='profile_pics')
    save_image1=models.BooleanField('', default=False)
    image2= models.ImageField(upload_to='profile_pics')
    save_image2=models.BooleanField('', default=False)
    is_checkbox2= models.BooleanField('Choose image 2 as profile picture, default profile picture is image 1', default=False)

    def save(self, **kwargs):
        import pdb
        pdb.set_trace()
        super().save()
        img= Image.open(self.image1.path)
        if img.height > 300 or img.width > 300:
            new_img = (1280, 960)
            img.thumbnail(new_img)
            img.save(self.image1.path) 
        img= Image.open(self.image2.path)
        if img.height > 300 or img.width > 300:
            new_img = (1280, 960)
            img.thumbnail(new_img)
            img.save(self.image2.path)
        if self.save_name:
            self.name=name

        