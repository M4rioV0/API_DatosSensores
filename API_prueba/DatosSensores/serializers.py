from models import Advice, AlertNo2, AlertO3, AlertPm2_5, AlertPm10, Avg8Hours, AvgDiary
from rest_framework import serializers

class AdviceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Advice
        fields=('advice','typeAdvice','idStation','value','timestamp')


class AlertNo2Serializer(serializers.ModelSerializer):
    class Meta:
        model= AlertNo2
        fields=('avgNo2','type','year1','idStation','subtype','timestamp')

class AlertO3Serializer(serializers.ModelSerializer):
    class Meta:
        model = AlertO3
        fields=('avgO3','idStation','subtype','timestamp','type','year1')

class AlertPm2_5Serializer(serializers.ModelSerializer):
    class Meta:
        model = AlertPm2_5
        fields=('avgPm2_5','idStation','timestamp','type')

class AlertPm10Serializer(serializers.ModelSerializer):
    class Meta:
        model = AlertPm10
        fields=('avgPm10','idStation','timestamp','type','year1')

class Avg8HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avg8Hours
        fields=('avgCo','avgO3','dateIni','idStation','timestamp')

class AvgDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AvgDiary
        fields=('avgCo','avgNo2','avgO3','avgPm1','avgPm10','avgPm2_5','dateIni','idStation', 'timestamp')

class AvgHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvgDiary
        fields=('avgPm10','avgNo2','avgCo','dateIni','idStation','avgPm2_5','avgO3','timestamp')