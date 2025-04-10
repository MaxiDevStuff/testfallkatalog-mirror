from django.shortcuts import render
from django.http import HttpResponse
from .models import Testfall
from django.template import loader


def index(request):
    testfaelle_liste = Testfall.objects.order_by("dateiname")[:5]
    template = loader.get_template("katalog/index.html")
    context = {"testfaelle_liste": testfaelle_liste}
    return HttpResponse(template.render(context, request))

def liste(request, test):
    response = "Du hast als test %s eingegeben"
    return HttpResponse(response % test)
