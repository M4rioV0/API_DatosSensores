from django.db import models

class Advice(models.Model):

    advice = models.CharField(max_length=20)
    typeAdvice = models.CharField(max_length=40)
    idStation = models.CharField(max_length=40)
    value = models.CharField(max_length=40)
    timestamp = models.DateTimeField()

class AirMeasurement(models.Model):
    baterryVolts = models.FloatField()
    batteryCurrent = models.FloatField()
    batteryLevel = models.FloatField()
    co = models.FloatField()
    coC = models.FloatField()
    date = models.BigIntegerField()
    humidity = models.FloatField()
    idStation = models.CharField(max_length=80)
    luminosity = models.FloatField()
    no2 = models.FloatField()
    no2C = models.FloatField()
    o3 = models.FloatField()
    o3C = models.FloatField()
    pm1 = models.FloatField()
    pm10 = models.FloatField()
    pm2_5 = models.FloatField()
    pressure = models.FloatField()
    serial = models.CharField(max_length=100)
    temperature = models.FloatField()
    timestamp = models.DateTimeField()
    timestampSensor = models.DateTimeField()

class AlertNo2(models.Model):
    avgNo2 = models.FloatField()
    type = models.CharField(max_length=40)
    year1 = models.IntegerField()
    idStation = models.CharField(max_length=40)
    subtype = models.CharField(max_length=40)
    timestamp = models.DateTimeField()

class AlertO3(models.Model):
    avgO3 = models.FloatField()
    idStation = models.CharField(max_length=40)
    subtype = models.CharField(max_length=40)
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=40)
    year1 = models.IntegerField()

class AlertPm2_5(models.Model):
    avgPm2_5 = models.FloatField()
    idStation = models.CharField(max_length=40)
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=40)

class AlertPm10(models.Model):
    avgPm10 = models.FloatField()
    idStation = models.CharField(max_length=40)
    timestamp = models.DateTimeField()
    type = models.CharField(max_length=40)
    year1 = models.IntegerField()

class Avg8Hours(models.Model):
    avgCo = models.FloatField()
    avgO3 = models.FloatField()
    dateIni = models.IntegerField()
    idStation = models.CharField(max_length=40)
    timestamp = models.DateTimeField()

class AvgDiary(models.Model):
    avgCo = models.FloatField()
    avgNo2 = models.FloatField()
    avgO3 = models.FloatField()
    avgPm1 = models.FloatField()
    avgPm10 = models.FloatField()
    avgPm2_5 = models.FloatField()
    dateIni = models.IntegerField()
    idStation = models.CharField(max_length=40)
    timestamp = models.DateTimeField()
    
class AvgHour(models.Model):
    avgPm10 = models.FloatField()
    avgNo2 = models.FloatField()
    avgCo = models.FloatField()
    dateIni = models.FloatField()
    idStation = models.FloatField()
    avgPm2_5 = models.FloatField()
    avgO3 = models.IntegerField()
    timestamp = models.DateTimeField()

class Danger(models.Model):
    max = models.FloatField()
    stations = models.CharField(max_length=800)
    times = models.IntegerField()
    min = models.FloatField()
    dangerType = models.CharField(max_length=400)
    timestamp = models.DateTimeField()

class Warning(models.Model):
    warningType = models.CharField(max_length=400)
    stations = models.CharField(max_length=800)
    timestamp = models.DateTimeField()

# Create your models here.
