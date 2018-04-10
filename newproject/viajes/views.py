from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from .models import Viaje, Cliente


formulario = """
<form action= "" method="POST">
 Destino: <input type="text" name="desti"><br>
 Locomocion: <input type="text" name="loco" value="Avion"><br>
 Alojamiento: <input type="text" name="aloja"><br>
 Precio: <input type="text" name="preci"><br>
 <input type="submit" name="Enviar">

"""


def barra(request):
    if request.user.is_authenticated():
        logged = 'Logged as '+ request.user.username
    else:
        logged = 'Not logged in.'

    viajes = Viaje.objects.all() # dame todos los viajes
				# me los devuelves en una lista
				# viaje.id, viaje.destino...
    respuesta = "<ul>"
    for viaje in viajes:
        respuesta += '<li><a href="/viajes/viaje/'+ str(viaje.id) + '">' + viaje.destino + '</a>'
    respuesta += "<ul>"

    return HttpResponse(logged + '<br>' + respuesta)



@csrf_exempt
def viaje(request, number):
    if request.method == "POST":
        viaje = Viaje(locomocion = request.POST["loco"], destino = request.POST["desti"], alojamiento = request.POST["aloja"], 
precio = request.POST["preci"])
        viaje.save() # Lo guarda en la base de datos
        number = viaje.id()

    try:
        viaje = Viaje.objects.get(id=int(number))
    except Viaje.DoesNotExist:
        return HttpResponse("No existe <br>" + formulario)
    respuesta = "Viaje: " + viaje.destino + "<br>"
    respuesta += "Precio: " + str(viaje.precio) + "<br>"
    respuesta += "ID: " + str(viaje.id) + "<br>"
    respuesta += "Locomocion: " + str(viaje.locomocion) + "euros <br><br>"
    respuesta += formulario
    return HttpResponse(respuesta)



def cliente(request, number):

    try:
        cliente = Cliente.objects.get(id=int(number))
    except Cliente.DoesNotExist:
        return HttpResponse("No existe")
    respuesta = "Cliente: " + cliente.nombre
    return HttpResponse(respuesta)


