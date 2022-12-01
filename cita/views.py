from django.shortcuts import render, redirect
from urllib.request import Request
from cita.forms import CitaForm, ServiciosForm, AgendaForm, FechaDisponibleForm
from cita.models import Cita, Servicio, Agenda
from datetime import datetime
from paciente.models import Paciente
from datetime import datetime
from django.contrib import messages


# Create your views here.


def cita(request):
    titulo = "Cita"
    cita = Cita.objects.all()
    context = {
        'titulo': titulo,
        'cita': cita

    }

    return render(request, "Cita/cita.html", context)


def cita_crear(request):
    titulo = "Agenda tu Cita"
    servicios = Servicio.objects.all()
    if request.method == "POST":
        print(request.POST)
        return redirect('crear-agenda', pk=request.POST['servicio'])
    else:
        form = FechaDisponibleForm()
    context = {
        "titulo": titulo,
        "form": form,
        "servicios": servicios
    }
    return render(request, 'Cita/cita.html', context)


def servicio(request):
    titulo = "Servicios"
    servicios = Servicio.objects.all()
    context = {
        'titulo': titulo,
        'servicios': servicios

    }

    return render(request, "Cita/servicios.html", context)


def servicios_crear(request):
    titulo = "Crear Servicio"
    if request.method == "POST":
        form = ServiciosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio-adm')
        else:
            print("Error")
    else:
        form = ServiciosForm()
    context = {
        "titulo": titulo,
        "form": form

    }
    return render(request, 'Cita/servicios.html', context)


def citas_listar(request):
    titulo = "Cita-listar"
    if request.user.groups.filter(name="Administrador").exists():
        citas = Cita.objects.all()
    else:
        citas = Cita.objects.filter(paciente__numDocumento=request.user.username)

    context = {
        'titulo': titulo,
        'citas': citas

    }

    return render(request, "Cita/buscarCita.html", context)


def modificar(request):
    titulo = "Modificar Cita"
    citas = Cita.objects.all()
    context = {
        'titulo': titulo,
        'citas': citas

    }

    return render(request, 'Cita/modificarCita.html', context)



def citas_modificar(request, pk,dia=None):
    titulo = "Modifica tu cita"
    cita =Cita.objects.get(id=pk)
    if request.method == "POST":
        form= CitaForm(request.POST,instance=cita)
        if form.is_valid():
            form.save
            messages.success(
                request, f"Se modificó su cita exitosamente"
            )
            return redirect('inicio-adm')
        else:
            print("Error al guardar")

    else:
        form=CitaForm(instance=cita)

        context={
        "titulo":titulo,
        "form":form
        
    }

    return render(request, 'Cita/modificarCita.html', context)


def citas_eliminar(request, pk):
    titulo = "Eliminar Cita"
    pacientes = Cita.objects.all()

    Cita.objects.filter(id=pk).update(
        estado='0'
    )
    messages.success(
                request, f"Se eliminó su cita exitosamente"
            )
    return redirect("inicio-adm")


def agenda(request):
    titulo = "Agenda"
    agenda = Agenda.objects.all()
    context = {
        'titulo': titulo,
        'agenda': agenda

    }

    return render(request, "Cita/agenda.html", context)


def agenda_crear(request, pk, fecha=None):
    servicio= Servicio.objects.get(id=pk)
    titulo = f"Agendar Cita para {servicio}"
    agendas = Agenda.objects.all().filter(fecha__servicio_id=int(
      pk), fecha__fecha__gte=datetime.today(),estado="1").values_list('fecha__fecha',flat=True).distinct()
    fechas=None
    if fecha:
      
        fechas= Agenda.objects.filter(fecha__fecha=fecha,fecha__servicio_id=int(
      pk),estado="1")
    if request.method == "POST" and 'form-fecha' in request.POST:
        fecha = request.POST['fecha']
        return redirect('crear-agenda', pk=pk, fecha=fecha)
    if request.method == "POST" and 'form-crear' in request.POST:

        agenda = Agenda.objects.get(fecha__fecha=fecha, horaDisponible=int(request.POST['horaDisponible']))
        cita = Cita.objects.create(
            agenda_id=agenda.id,
            paciente=Paciente.objects.get(user_id=request.user.id)
        )
        agenda.estado="0" 
        agenda.save()   
        messages.success(
                request, f"Se agendó su cita exitosamente"
            )
        return redirect("inicio-adm")
    context = {
        "titulo": titulo,
        "agendas": agendas,
        "fecha": fecha,
        "fechas":fechas
    }
    return render(request, 'Cita/agenda.html', context)
