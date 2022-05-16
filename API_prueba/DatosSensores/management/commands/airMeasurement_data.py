from re import sub
from django.core.management.base import BaseCommand
import json
from datetime import datetime
from DatosSensores.models import AirMeasurement

data = open("C://Users\mario\dev\API\API_prueba\data\AirMeasurement.json","r")

x = data.read()

data.close()

json_ = json.loads(x)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for linea in json_:

            batteryVolts = linea["batteryVolts"]
            batteryCurrent = linea["batteryCurrent"]
            batteryLevel = linea["batteryLevel"]
            co = linea["co"]
            coC = linea["coC"]
            date = linea["date"]
            humidity = linea["humidity"]
            idStation = linea["idStation"]
            luminosity = linea["luminosity"]
            no2 = linea["no2"]
            no2C = linea["no2C"]
            o3 = linea["o3"]
            o3C = linea["o3C"]
            pm1 = linea["pm1"]
            pm10 = linea["pm10"]
            pm2_5 = linea["pm2_5"]
            pressure = linea["pressure"]
            serial = linea["serial"]
            temperature = linea["temperature"]
            timestamp = linea["timestamp"]
            timestampSensor = linea["timestampSensor"]

            timestamp = timestamp/1000
            timestampSensor = timestampSensor/1000

            tt = datetime.fromtimestamp(timestamp)
            tts = datetime.fromtimestamp(timestampSensor)

            airMeasurements  = AirMeasurement(
            
                batteryVolts = batteryVolts,
                batteryCurrent = batteryCurrent,
                batteryLevel = batteryLevel,
                co = co,
                coC = coC,
                date = date,
                humidity = humidity,
                idStation = idStation,
                luminosity = luminosity,
                no2 = no2,
                no2C = no2C,
                o3 = o3,
                o3C = o3C,
                pm1 = pm1,
                pm10 = pm10,
                pm2_5 = pm2_5,
                pressure = pressure,
                serial = serial,
                temperature = temperature,
                timestamp = timestamp,
                timestampSensor = timestampSensor
                
            )
    
            airMeasurements.save()
        self.stdout.write(self.style.SUCCESS('Datos importados de forma correcta '))