from re import sub
from django.core.management.base import BaseCommand
import json
from datetime import datetime
from DatosSensores.models import AlertO3

data = open("C://Users\mario\dev\API\API_prueba\data\AlertO3.json","r")

x = data.read()

data.close()

json_ = json.loads(x)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for linea in json_:

            avg03 = linea["advice"]
            idStation = linea["idStation"]
            subtype = linea["subtype"]
            timestamp = linea["timestamp"]
            type = linea["type"]
            year1 = linea["year1"]

            timestamp = timestamp/1000

            tt = datetime.fromtimestamp(timestamp)

            alerto3  = AlertO3(
            
                avg03 = avg03,
                idStation = idStation,
                subtype = subtype,
                timestamp = tt,
                type = type,
                year1 = year1
                
            )
    
            alerto3.save()
        self.stdout.write(self.style.SUCCESS('Datos importados de forma correcta '))