from re import sub
from django.core.management.base import BaseCommand
import json
from datetime import datetime
from DatosSensores.models import AlertPm10

data = open("C://Users\mario\dev\API\API_prueba\data\AlertPm10.json","r")

x = data.read()

data.close()

json_ = json.loads(x)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for linea in json_:

            avgPm10 = linea["avgPm10"]
            idStation = linea["idStation"]
            timestamp = linea["timestamp"]
            type = linea["type"]
            year1 = linea["year1"]

            timestamp = timestamp/1000

            tt = datetime.fromtimestamp(timestamp)

            alertpm10  = AlertPm10(
            
                avgPm10 = avgPm10,
                idStation = idStation,
                timestamp = tt,
                type = type,
                year1 = year1
                
            )
    
            alertpm10.save()
        self.stdout.write(self.style.SUCCESS('Datos importados de forma correcta '))