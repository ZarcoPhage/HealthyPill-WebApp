from django.http import HttpResponse
from django.template import Template, Context

def holi(request):
    docPlantilla = open("C:/Users/Moonlabpc/Desktop/ProyectoIntro/HealthyPillMain/HealthyPillMain/plantillas/saludito.html")
    
    plantillaHoli = Template(docPlantilla.read())

    docPlantilla.close()

    contextoPlantilla=Context({"saludo": "hola"})

    plantillaFinal = plantillaHoli.render(contextoPlantilla)

    return HttpResponse(plantillaFinal)