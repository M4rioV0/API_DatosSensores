from django.urls import path,include
from . import views

urlpatterns = [
    path('advice', views.advice_list_create_view),
    path('alertNo2', views.alertNo2_list_create_view),
    path('alertO3', views.alertO3_list_create_view),
    path('alertPm10', views.alertPm10_list_create_view),
    path('avg8Hours', views.avg8Hours_list_create_view),
    path('avgDiary', views.avgDiary_list_create_view),
    path('AvgHour', views.avgHour_list_create_view),
]