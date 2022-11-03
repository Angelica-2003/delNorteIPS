
from urllib.request import Request
from django.shortcuts import  redirect,render


from paciente.forms import PacienteForm, PacienteUpdateForm
from paciente.models import Paciente

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.

# def pacientes(request):
#     titulo="Paciente"
#     pacientes= Paciente.objects.all()
#     context={
#         'titulo':titulo,
#         'pacientes':pacientes
        
#     }

#     return render(request,"listar.html",context)

@login_required(login_url="incio")
def pacientes_crear(request):
    titulo="Crear Paciente"
    if request.method == "POST":
        form= PacienteForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=request.POST["numDocumento"]):
                user= User.objects.create_user("nombre","email","pass")
                user.username=request.POST["numDocumento"]
                user.first_name=request.POST["nombres"].title()
                user.last_name=request.POST["apellidos"].title()
                user.email=request.POST["email"]
                user.password=make_password("@" + request.POST['nombres'][0] + request.POST['apellidos'][0] + request.POST['numDocumento'][-4:])
                user.save()
            else:
                user=User.objects.get(username=request.POST["numDocumento"])

            paciente=Paciente.objects.create(
                nombres=request.POST["nombres"],
                apellidos=request.POST["apellidos"],
                tipoDocumento=request.POST["tipoDocumento"],
                numDocumento=request.POST["numDocumento"],
                rh=request.POST["rh"],
                telefono=request.POST["telefono"],
                email=request.POST["email"],
                fechaNacimiento=request.POST["fechaNacimiento"],
                nombreContacto=request.POST["nombreContacto"],
                telefonoContacto=request.POST["telefonoContacto"],
                user=user,

            )
            return redirect('login')

        else:
            form = PacienteForm(request.POST)
    else:
        form= PacienteForm()
    context={
        "titulo":titulo,
        "form":form
        
    }
    return render(request,'pacientes-crear.html',context)


def pacientes(request, modal_status="hid"):
    titulo="Crear Pacientes"
    pacientes= Paciente.objects.filter(estado="1")

    ###### Cuerpo del modal ##########
    modal_title=""
    modal_txt=""
    modal_submit=""
    ###################################
    pk_paciente = ""
    tipo =None
    form_update=None
    form =PacienteForm()

    if request.method == "POST" and "form-crear" in request.POST:
        form= PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form= PacienteForm(request.POST)
            messages.error(
                request, "Error al agregar el paciente"
            )

############################## Configuracion modal de eliminacion ###################


    if request.method == "POST" and "form-eliminar" in request.POST:
        modal_status= "show"
        pk_paciente = request.POST["pk"]
        paciente=Paciente.objects.get(id=pk_paciente)

        ###### Cuerpo del mmodal ########
        modal_title = f"eliminar (paciente)"
        modal_txt= f"Eliminar el Paciente"
        modal_submit= "Aceptar"
        ######################################

        tipo="eliminar"
        ############################ Configuracion modal de edicion ###################
    if request.method == "POST" and "form-editar" in request.POST:
        modal_status= "show"
        pk_paciente = request.POST["pk"]
        paciente=Paciente.objects.get(id=pk_paciente)

        ###### Cuerpo del mmodal ########
        modal_title = f"Editar (paciente)"
        modal_submit= "Editar el paciente"
        ######################################

        tipo="editar"
    
        form_update= PacienteUpdateForm(instance=paciente)

############################ Configuracion de eliminacion ###################

    if request.method == "POST" and "modal-confirmar" in request.POST:
        if request.POST["tipo"]=="eliminar":
            paciente = Paciente.objects.filter(id = int(request.POST["modal-pk"])).update(
                estado="0"

            )
            messages.success(
                request, f"Se eliminò el paciente exitosamente!"
            )

            return redirect("inicio-adm")

        if request.POST["tipo"]=="editar":
            pk_paciente = request.POST["modal-pk"]
            paciente=Paciente.objects.get(id=pk_paciente)
            form_update=PacienteUpdateForm(request.POST, instance=paciente)

            if form_update.is_valid():
                form_update.save()

            messages.success(
                request, f"Se editò el paciente exitosamente!"
            )
            return redirect("inicio-adm")
        
            
    context={

        "titulo":titulo,
        "pacientes":pacientes,
        'form':form,

        "modal_status":modal_status,
        "modal_submit":modal_submit,
        "modal_title":modal_title,
        "modal_txt":modal_txt,
        "pk":pk_paciente,
        "tipo":tipo,
        "form_update":form_update
        
    }
    return render(request,'listar.html',context)




