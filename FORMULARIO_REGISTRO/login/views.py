from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models

#Variables globales que serán utilizadas para el control
#de inicio de cesion. Estas controlarán los saltos de vistas a 
# traves de las urls para que el usuario no pueda controlar
#estas transiciones a su conveniencia.
logueado = 0
usuario_logueado = ""

# Create your views here.
def loguearse(request):
    global logueado, usuario_logueado

    #Si el usuario ya está logueado lo redirige
    if logueado == 1:
        return redirect("inicio/%s"%usuario_logueado)

    if request.method == "POST":
        #Se inicializa la variable de control de errores con sus valores en 0.
        errores= {
            "usuario" : 0,
            "clave"   : 0,
            "no_existe" : 0,
            "clave_incorrecta" : 0
        }

        #En caso de error al recargar la pagina se rellenaran los textbox que ya
        #fueron llenados
        datos_actuales = {
            "usuario": request.POST.get("usuario"),
        }

        usuario = request.POST.get("usuario")
        clave   = request.POST.get("clave")

        #Se comienzan a filtrar posibles errores que ocurren
        #al momento  de querer loguearse
        if(usuario!="" and clave!="" ):
            consulta_usuario = models.Usuario.objects.filter(nombre=usuario)

            #Si el usuario existe se consulta si es la contraseña correcta
            if(len(consulta_usuario) == 1):
                usuarioBD = models.Usuario.objects.get(nombre=usuario)

                if(clave == usuarioBD.clave):
                    logueado = 1
                    usuario_logueado = usuario
                    return redirect("inicio/%s"%usuario)
                else:
                    errores["clave_incorrecta"] = 1
            else:
                errores["no_existe"] = 1
        else:
            if usuario == "":
                errores["usuario"] = 1

            if clave == "":
                errores["clave"] = 1

        return render(request, "login.html", {"errores": errores, "datos_llenados": datos_actuales})

    return render(request, "login.html", {"errores": "", "datos_llenados": ""})

def registrarse(request):
    global logueado, usuario_logueado
    
    #Si el usuario ya está logueado lo redirige
    if logueado == 1:
        return redirect("inicio/%s"%usuario_logueado)

    if request.method == "POST":
        #Se inicializa la variable de control de errores con sus valores en 0.
        errores= {
            "usuario" : 0,
            "clave"   : 0,
            "clave2"  : 0,
            "clave_distinta" : 0,
            "existe" : 0
        }

        #En caso de error al recargar la pagina se rellenaran los textbox que ya
        #fueron llenados
        datos_actuales = {
            "usuario": request.POST.get("usuario"),
        }

        usuario = request.POST.get("usuario")
        clave   = request.POST.get("clave")
        clave2  = request.POST.get("clave2")

        #Se comienzan a filtrar posibles errores que ocurren al momento 
        #de querer crear el usuario
        if(usuario!="" and clave!="" and clave2!=""):
            consulta_usuario = models.Usuario.objects.filter(nombre=usuario)

            #Si el usuario existe será notificado
            if(len(consulta_usuario) == 0):
                if(clave == clave2):
                    nuevo_usuario = models.Usuario(nombre=usuario, clave=clave)
                    nuevo_usuario.save()
                    return redirect("loguearse")
                else:
                    errores["clave_distinta"] = 1
            else:
                errores["existe"] = 1
        else:
            if usuario == "":
                errores["usuario"] = 1

            if clave == "":
                errores["clave"] = 1
            
            if clave2 == "":
                errores["clave2"] = 1

        return render(request, "registrarse.html", {"errores": errores, "datos_llenados": datos_actuales})


    return render(request, "registrarse.html", {"errores":"", "datos_llenados":""})

def mostrar_inicio(request, usuario):
    global logueado
    
    #Si el usuario no está logueado lo redirige
    if logueado == 0:
        return redirect("loguearse")

    return render(request, "pagina/saludo.html", {"usuario": usuario})

def cerrar_sesion(request):
    global logueado
    logueado = 0
    return redirect("loguearse")