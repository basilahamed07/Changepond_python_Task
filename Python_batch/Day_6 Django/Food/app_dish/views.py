from django.shortcuts import render
from django.http import *



def app_dis(request,dish):
    if dish == "dosai":
        return HttpResponse("Dosai here")
    elif dish == "vadai":
        return HttpResponse("vadai vadai here")
    elif dish == "mandi":
        return HttpResponse("mandi here")
    elif dish == "vadai_vadai":
        return HttpResponse("vadai super")
    else:
        return HttpResponse("not found")