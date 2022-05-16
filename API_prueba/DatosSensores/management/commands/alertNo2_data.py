from re import sub
from django.core.management.base import BaseCommand
import json
from datetime import datetime
from DatosSensores.models import AlertNo2

data = open("C://Users\mario\dev\API\API_prueba\data\AlertNo2.json","r")

x = data.read()

data.close()

json_ = json.loads(x)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for linea in json_:

            avgNo2 = linea["avgNo2"]
            idStation = linea["idStation"]
            subtype = linea["subtype"]
            timestamp = linea["timestamp"]
            type = linea["type"]
            year1 = linea["year1"]

            timestamp = int(timestamp)
            timestamp = timestamp/1000

            tt = datetime.fromtimestamp(timestamp)

            alertno2  = AlertNo2(
            
                avgNo2 = avgNo2,
                type = type,
                year1 = year1,
                idStation = idStation,
                subtype = subtype,
                timestamp = tt
                
            )
    
            alertno2.save()
        self.stdout.write(self.style.SUCCESS('Datos importados de forma correcta '))