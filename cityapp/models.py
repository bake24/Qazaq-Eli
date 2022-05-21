from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class City(models.Model):
    title = models.CharField('City name', max_length=20)
    est = models.IntegerField('Est year')
    description = models.TextField('Description')
    def __str__(self):
       return self.title

    class Meta:
         verbose_name = "Қала"
         verbose_name_plural = "Қалалар"



class Contact(models.Model):
    name = models.CharField('Name', max_length=50)
    country = models.CharField('Country', max_length=50)
    telnumber = models.IntegerField('Telephone number')
    def __str__(self):
       return self.name


    class Meta:
         verbose_name = "Ақпарат"
         verbose_name_plural = "Ақпарат"



class Place(models.Model):
    cityname = models.CharField('City Name', max_length=30)
    place1 = models.CharField('Place1', max_length=30)
    place2= models.CharField('Place2', max_length=15)
    place3 = models.CharField('Place3', max_length=100)

    # cat = models.ForeignKey('Category', on_delete=models.Project, verbose_name="Category")
    def __str__(self):
       return self.cityname

    class Meta:
         verbose_name = "Демалыс Орын"
         verbose_name_plural = "Демалыс Орындар"


class Famous(models.Model):
    city_name = models.CharField('City name', max_length=30)
    pers1 = models.CharField('Pers1', max_length=30)
    pers2= models.CharField('Pers2', max_length=30)
    pers3 = models.CharField('Pers3', max_length=100)
    def __str__(self):
       return self.city_name

    #dwqwdqwd#


    class Meta:
         verbose_name = "Танымал адамдар"
         verbose_name_plural = "Танымал адамдар"


class Register(models.Model):


    name = models.CharField('Name', max_length=30)
    surname = models.CharField('Surname', max_length=30)
    country = models.CharField('Country', max_length=30)
    desired_city = models.CharField('Des City', max_length=100)
    desired_place = models.CharField('Des Place', max_length=100)
    date = models.DateField('Date')
    card_num = models.IntegerField('Card number')
    email = models.CharField('Email', max_length=31)
    image = models.ImageField(upload_to='media/images')


    def __str__(self):
       return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



