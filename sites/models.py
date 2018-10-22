from django.db import models

# Create your models here.
class SiteDetail(models.Model):
    siteNumber = models.IntegerField()
    siteName = models.CharField(max_length=200)
    timezone = models.TimeField(default='08:00')
    path = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.siteName)

class WMO(models.Model):
    siteNumber = models.OneToOneField(SiteDetail, on_delete=models.CASCADE)
    wmoNumber = models.IntegerField()

    def __str__(self):
        return str(self.wmoNumber)


class Aviation(models.Model):
    siteNumber = models.OneToOneField(SiteDetail, on_delete=models.CASCADE)
    ident = models.CharField(max_length=30)

    def __str__(self):
        return self.ident

class Equipment(models.Model):
    site = models.ManyToManyField(SiteDetail)


class NetworkDevice(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name

	
class Comms(Equipment):
    levelChoice = (
        ('primary', 'primary'),
        ('secondary', 'secondary'),
        ('tertiary', 'tertiary'),
        ('standalone', 'standalone'),
    )
    level = models.CharField(max_length=200, choices=levelChoice)
    netAddress = models.CharField(max_length=30, null=True)
    networkDevice = models.ForeignKey('NetworkDevice', related_name='commDevice', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.networkDevice.name

class Radar(Equipment):
    radarChoice = (
        ('2502', '2502'),
        ('Wurrung', 'Wurrung'),
        ('5C', '5C'),
        ('6C', '6C'),
        ('Selex', 'Selex'),
    )
    IDR = models.IntegerField()
    radarModel = models.CharField(max_length=30, choices=radarChoice)

    def __str__(self):
        return self.radarModel


class AWS(Equipment):
    adjChoice = (
        ('true', 'yes'),
        ('false', 'no'),
    )
    awsType = (
        ('Almos', 'Almos'),
        ('Telvent', 'Telvent'),
    )
    powerChoice = (
        ('mains', 'mains'),
        ('solar', 'solar'),
    )
    timeAdj = models.CharField(max_length=5, choices=adjChoice)
    AWSModel = models.CharField(max_length=30, choices=awsType)
    power = models.CharField(default='mains',max_length=30, choices=powerChoice)
    port = models.IntegerField(default=1516)
    gateway = models.ForeignKey('Comms', related_name='AWS_gw', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.AWSModel

