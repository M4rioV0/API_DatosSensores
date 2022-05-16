from re import sub
from django.core.management.base import BaseCommand
import json
from datetime import datetime
from DatosSensores.models import AlertPm2_5

data = open("C://Users\mario\dev\API\API_prueba\data\AlertPm2_5.json","r")

x = data.read()

data.close()

json_ = json.loads(x)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for linea in json_:

            avgPm2_5 = linea["avgPm2_5"]
            idStation = linea["idStation"]
            timestamp = linea["timestamp"]
            type = linea["type"]

            timestamp = timestamp/1000

            tt = datetime.fromtimestamp(timestamp)

            alertpm2_5  = AlertPm2_5(
            
                avgPm2_5 = avgPm2_5,
                idStation = idStation,
                timestamp = tt,
                type = type
                
            )
    
            alertpm2_5.save()
        self.stdout.write(self.style.SUCCESS('Datos importados de forma correcta '))