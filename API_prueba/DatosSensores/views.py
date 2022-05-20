from multiprocessing import context
from re import A
from django.db.models import Q, Count
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Advice
from django.contrib.auth import logout

#--METODO PARA VALIDAR LOS DATOS--#
def is_valid_queryparam(param):
    return param != '' and param is not None

#--VISTA DEL INICIO--#
def HomeView(request):
    return render(request, "home.html")

#--VISTA DE LOG OUT--#
def LogOutUser(request):
    logout(request)
    return redirect('sign_in')

#--QUERY DE LOS DATOS DE ADVICE--#

def AdiceFilter(request):
    qs = Advice.objects.all()
    advice = request.GET.get('advice')

    if is_valid_queryparam(advice) and advice != 'Choose...':
        qs = qs.filter(advice__advice=advice)

    return qs

def AdviceFilterView(request):
    qs = filter(request)
    context = {
        'queryset': qs,
    }
    return render(request, "bootstrap_form.html", context)
