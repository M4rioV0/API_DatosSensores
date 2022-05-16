from logging import warning
from re import sub
from django.core.management.base import BaseCommand
import json
from datetime import datetime
from DatosSensores.models import Warning

data = open("C://Users\mario\dev\API\API_prueba\data\Warning.json","r")

x = data.read()

data.close()

json_ = json.loads(x)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for linea in json_:

            warningType = linea["warningType"]
            stations = linea["stations"]
            timestamp = linea["timestamp"]
            
            timestamp = timestamp/1000

            tt = datetime.fromtimestamp(timestamp)

            avg8hours  = Warning(
            
                warningType = warningType,
                stations = stations,
                timestamp = timestamp
                
            )
    
            avg8hours.save()
        self.stdout.write(self.style.SUCCESS('Datos importados de forma correcta '))