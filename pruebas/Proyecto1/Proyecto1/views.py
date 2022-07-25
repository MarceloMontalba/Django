# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 18:46:41 2022

@author: nehemias
"""

#Pruebas con Plantillas 

from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre   = nombre;
        self.apellido = apellido
    
#Vista para probar el uso de plantillas
def saludar(request):
    domExterno = open("Proyecto1/plantillas/saludo.html")
    verDom = Template(domExterno.read())
    domExterno.close()
    contexto = Context()
    
    miDOM = verDom.render(contexto)
    return HttpResponse(miDOM)

#Vista para probar el uso de plantillas y el uso de diccionarios en ellas
def despedir(request):
    nombre = "Raul"
    apellido = "Montes"
    persona2 = Persona("Juan","Zapata")
    
    fechaActual = datetime.datetime.now()
    
    domExterno = open("Proyecto1/plantillas/despedida.html")
    verDom = Template(domExterno.read())
    domExterno.close()
    contexto = Context({"nombre_persona1": nombre, 
                        "apellido_persona1" : apellido,
                        "nombre_persona2": persona2.nombre, 
                        "apellido_persona2" : persona2.apellido,
                        "momento_actual"    : fechaActual
                        })
    
    miDOM = verDom.render(contexto)
    return HttpResponse(miDOM)

#Vista para devolver fecha y hora actuales
def verFechaHora(request):
    fechaActual = datetime.datetime.now()
    
    miDOM = '''
    <html>
        <h1>
            Fecha y Hora Actuales %s
        </h1>
    </html>
    ''' %fechaActual
    return HttpResponse(miDOM)

#Vista que calcula la edad futura de alguien
#al recibir como parametros la edad actual y el año
#deseado.
def calcularEdad(request, edadActual, agno):
    periodo    = agno - 2022
    edadFutura = edadActual + periodo
    miDOM = '''
    <html>
        <body>
            <h2>
                En el año %s la edad que tendrás será de %s años
            </h2>
        </body>
    </html>
    ''' %(agno, edadFutura)
    
    return HttpResponse(miDOM)
    
#Vista de prueba para probar el uso de listas, condicionales, filtros
# y ciclos en las planillas. Cargadores de Plantillas
def llamarMetodosPlantilla(request):
    #Esta es una forma tosca de cargar una plantilla:
        #domExterno = open("Proyecto1/plantillas/llamando_metodos_plantilla.html")
        #verDom = Template(domExterno.read())
        #domExterno.close()
        #contexto = Context({"nombre_persona": persona1.nombre,"temas": temas})
        #miDom = verDom.render(contexto)
        #return HttpResponse(miDom)
        
    #Otra forma se realiza con loader.get_template:
        #domExterno = loader.get_template("llamando_metodos_plantilla.html")
        #miDom = domExterno.render({"nombre_persona": persona1.nombre,"temas": temas})
        #return HttpResponse(miDom)
        
    persona1 = Persona("Marcelo", "Montalba")
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]
    
    #Tercera forma de hacerlo y la mas eficiente, ya que se hace en una linea con render:
    return render(request, "llamando_metodos_plantilla.html", {"nombre_persona": persona1.nombre,"temas": temas})
    
def llamarPlantillasIncrustadas(request):
    persona1 = Persona("Marcelo", "Montalba")
    return render(request, "llamando_barra.html", 
                  {
                      "nombre_persona": persona1.nombre,
                      "apellido_persona": persona1.apellido
                  })       

def llamarHijo(request):
    fechaActual = datetime.datetime.now()
    return render(request, "hijo1.html", {"fecha": fechaActual})
    
    
    
    

