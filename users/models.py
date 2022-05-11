from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)# CASCADE purpose : once we delete the user then also delete the profile, but if we delete the profile we won't delete the user.
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pics')#upload_to is a path that the image stored 


    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kawrgs):#it's a method that taht gets to run after our model is save , it's a method already exist in our parent class
        super().save(*args, **kawrgs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)