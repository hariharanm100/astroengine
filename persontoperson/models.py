from django.db import models

# Create your models here.
class concatenation_points(models.Model):
    con_type = models.CharField(max_length=20)
    con_name = models.CharField(max_length=20)
    con_points = models.FloatField()

    def __str__(self):
        return self.con_type

class distance_multiplier(models.Model):
    distance = models.FloatField()
    multiplier = models.FloatField()

    def __str__(self):
        return str(self.distance)


class plotimages(models.Model):
    img_conj = models.ImageField(blank=True)
    img_180 = models.ImageField(blank=True)
    img_120l = models.ImageField(blank=True)
    img_120g = models.ImageField(blank=True)
    img_90l = models.ImageField(blank=True)
    img_90g = models.ImageField(blank=True)
    img_60l = models.ImageField(blank=True)
    img_60g = models.ImageField(blank=True)
    img_150 = models.ImageField(blank=True)

class birthchartdb(models.Model):
    fullname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    time_of_birth = models.TimeField()
    place_of_birth = models.CharField(max_length=100)
    coordinates_lan = models.FloatField(blank=True,null=True)
    coordinates_lon = models.FloatField(blank=True,null=True)
    time_zone = models.CharField(max_length=100,blank=True,null=True)
    timeZoneId = models.CharField(max_length=100,blank=True,null=True)
    timeZoneName = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.fullname
class PersonDegree(models.Model):
    personName = models.CharField(max_length=100)
    suDegree = models.FloatField()
    moDegree = models.FloatField()
    meDegree = models.FloatField()
    maDegree = models.FloatField()
    juDegree = models.FloatField()
    veDegree = models.FloatField()
    saDegree = models.FloatField()
    raDegree = models.FloatField()
    keDegree = models.FloatField()
    asDegree = models.FloatField()

    def __str__(self):
        return self.personName


class GlobalDegree(models.Model):
    suDegree = models.FloatField()
    moDegree = models.FloatField()
    meDegree = models.FloatField()
    maDegree = models.FloatField()
    juDegree = models.FloatField()
    veDegree = models.FloatField()
    saDegree = models.FloatField()
    raDegree = models.FloatField()
    keDegree = models.FloatField()
    asDegree = models.FloatField()

    def __str__(self):
        return str(self.id)
