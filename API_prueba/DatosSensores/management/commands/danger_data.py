from re import sub
from django.core.management.base import BaseCommand
import json
from datetime import datetime
from DatosSensores.models import Danger

data = open("C://Users\mario\dev\API\API_prueba\data\Danger.json","r")

x = data.read()

data.close()

json_ = json.loads(x)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for linea in json_:

            max = linea["max"]
            stations = linea["stations"]
            times = linea["times"]
            min = linea["min"]
            dangerType = linea["dangerType"]
            timestamp = linea["timestamp"]
            
            timestamp = timestamp/1000

            tt = datetime.fromtimestamp(timestamp)

            danger  = Danger(
            
                max = max,
                stations = stations,
                times = times,
                min = min,
                dangerType = dangerType,
                timestamp = tt
                
            )
    
            danger.save()
        self.stdout.write(self.style.SUCCESS('Datos importados de forma correcta '))