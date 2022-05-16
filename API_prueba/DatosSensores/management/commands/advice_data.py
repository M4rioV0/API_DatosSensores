from django.core.management.base import BaseCommand
import json
from datetime import datetime
from DatosSensores.models import Advice

data = open("C://Users\mario\dev\API\API_prueba\data\Advice.json","r")

a = data.read()

data.close()

json_ = json.loads(a)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for linea in json_:

            advice = linea["advice"]
            typeAdvice = linea["typeAdvice"]
            idStation = linea["idStation"]
            value = linea["value"]
            timestamp = linea["timestamp"]

            timestamp = timestamp/1000

            tt = datetime.fromtimestamp(timestamp)

            advice  = Advice(
            
                advice = advice,
                typeAdvice = typeAdvice,
                idStation = idStation,
                value = value,
                timestamp = tt,

            )
    
            advice.save()
        self.stdout.write(self.style.SUCCESS('Datos importados de forma correcta '))