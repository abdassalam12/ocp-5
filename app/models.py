from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    Image_RELATION =models.ForeignKey(User,on_delete=models.CASCADE)
    Image = models.ImageField(null=True,upload_to="images/",default="images/B.jpg")
class Own_Message(models.Model):
    Message_RELATION = models.ForeignKey(User,on_delete =models.CASCADE)
    Message = models.CharField(max_length=15000)
    lmoursil =models.CharField(max_length=15000)
    lmousta9bil =models.CharField(max_length=15000)
class decouvrir(models.Model) :
    caption = models.CharField(max_length=150)
    DecouvreImage = models.ImageField()
class offrefield(models.Model):
    id = models.IntegerField(primary_key=True)
    ImageDoffre = models.ImageField(null=False,upload_to='images/')
    reduction = models.IntegerField(null = True, default=0)
class bangalo(models.Model):
    ImageBangalo = models.ImageField(null=False,upload_to='images/')
    PlaceRestante = models.IntegerField(null = True, default=0)
    ville = models.CharField(null=False,default="safi")

# Create your models here.
 