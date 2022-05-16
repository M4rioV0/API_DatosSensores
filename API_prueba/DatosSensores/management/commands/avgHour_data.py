from re import sub
from django.core.management.base import BaseCommand
import json
from datetime import datetime
from DatosSensores.models import Avg8Hours

data = open("C://Users\mario\dev\API\API_prueba\data\AvgDiary.json","r")

x = data.read()

data.close()

json_ = json.loads(x)

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for linea in json_:

            avgPm10 = linea["avgPm10"]
            avgNo2 = linea["avgNo2"]
            avgCO = linea["avgCO"]
            dateIni = linea["dateIni"]
            idStation = linea["idStation"]
            avgPm2_5 = linea["avgPm2_5"]
            avgO3 = linea["avgO3"]
            timestamp = linea["timestamp"]
            
            dateIni = dateIni/1000
            timestamp = timestamp/1000

            di = datetime.fromtimestamp(dateIni)
            tt = datetime.fromtimestamp(timestamp)

            avg8hours  = Avg8Hours(
            
                avgPm10 = avgPm10,
                avgNo2 = avgNo2,
                avgCO = avgCO,
                dateIni = di,
                idStation = idStation,
                avgPm2_5 = avgPm2_5,
                avgO3 = avgO3,
                timestamp = tt
                
            )
    
            avg8hours.save()
        self.stdout.write(self.style.SUCCESS('Datos importados de forma correcta '))