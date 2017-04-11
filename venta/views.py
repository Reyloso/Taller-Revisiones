from django.shortcuts import render
from .models import Cliente, Auto, Consecionario, Revision
from .forms import forms_auto, forms_cliente, forms_revision, forms_consecionario
from django.shortcuts import get_object_or_404

# Create your views here.

def lista_autos(request):

    a = Auto.objects.all()

    return render(request,'venta/lista_autos.html',{'a':a})

def lista_cliente(request):

    a = Cliente.objects.all()

    return render(request,'venta/lista_cliente.html',{'a':a})

def lista_consecionario(request):

    a = Consecionario.objects.all()

    return render(request,'venta/lista_consecionario.html',{'a':a})

def lista_revision(request):

    a =Revision.objects.all()

    return render(request,'venta/lista_revision.html',{'a':a})


def lista_revision_auto(request,id):
    auto = Auto.objects.get(pk=id)
    a = Revision.objects.filter()



    return render(request,'venta/lista_revisiones_auto.html',{'a':a, 'auto':auto})


def crear_auto(request):
    formAuto = forms_auto()
    if request.method=="POST":
        formAuto = forms_auto(request.POST)
        if formAuto.is_valid():
            formAuto.save()
            a = Auto.objects.all()
            return render(request,'venta/lista_autos.html',{'a':a})


    return render(request, "venta/nuevo_auto.html", {"formAuto":formAuto })

def crear_cliente(request):
    formCliente = forms_cliente()
    if request.method=="POST":
        formCliente = forms_cliente(request.POST)
        if formCliente.is_valid():
            formCliente.save()
            a = Cliente.objects.all()
            return render(request,'venta/lista_cliente.html',{'a':a})



    return render(request, "venta/nuevo_cliente.html", {"formCliente":formCliente })

def crear_consecionario(request):
        formconsecionario = forms_consecionario()
        if request.method=="POST":
            formconsecionario = forms_consecionario(request.POST)
            if formconsecionario.is_valid():
                formconsecionario.save()
                a = Consecionario.objects.all()
                return render(request,'venta/lista_consecionario.html',{'a':a})


        return render(request, "venta/nuevo_consecionario.html", {"formconsecionario":formconsecionario })


def crear_revision(request):
        formrevision = forms_revision()
        if request.method=="POST":
            formrevision = forms_revision(request.POST)
            if formrevision.is_valid():
                formrevision.save()
                a = Revision.objects.all()
                return render(request,'venta/lista_revision.html',{'a':a})


        return render(request, "venta/nueva_revision.html", {"formrevision":formrevision })

def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, pk=id)
    a = auto
    if request.method=="POST":
        auto.delete()
        a = Auto.objects.all()
        return render(request,'venta/lista_autos.html',{'a':a})

    return render(request, "venta/eliminar_auto.html", {"a":a})

def eliminar_cliente(request, nid):
    cliente = get_object_or_404(Cliente, pk=nid)
    a = cliente
    if request.method=="POST":
        cliente.delete()
        a = Cliente.objects.all()
        return render(request,'venta/lista_cliente.html',{'a':a})

    return render(request, "venta/eliminar_cliente.html", {"a":a})

def eliminar_consecionario(request, nit):
        consecionario = get_object_or_404(Consecionario, pk=nit)
        a = consecionario
        if request.method=="POST":
            consecionario.delete()
            a = Consecionario.objects.all()
            return render(request,'venta/lista_consecionario.html',{'a':a})

        return render(request, "venta/eliminar_consecionario.html", {"a":a})

def eliminar_revision(request, id):
        revision = get_object_or_404(Revision, pk=id)
        a = revision
        if request.method=="POST":
            revision.delete()
            a = Revision.objects.all()
            return render(request,'venta/lista_revision.html',{'a':a})

        return render(request, "venta/eliminar_revision.html", {"a":a})


def modificar_auto(request,id):
    auto = get_object_or_404(Auto, pk=id)
    formAuto = forms_auto(request.POST or None, instance=auto)
    if request.method == "POST":
        if formAuto.is_valid():
            formAuto.save()
            a = Auto.objects.all()
            return render(request,'venta/lista_autos.html',{'a':a})


    return render(request, "venta/modificar_auto.html", {"formAuto":formAuto})

def modificar_cliente(request,nid):
    cliente = get_object_or_404(Cliente, pk=nid)
    formCliente = forms_cliente(request.POST or None, instance=cliente)
    if request.method == "POST":
        if formCliente.is_valid():
            formCliente.save()
            a = Cliente.objects.all()
            return render(request,'venta/lista_cliente.html',{'a':a})


    return render(request, "venta/modificar_cliente.html", {"formCliente":formCliente})

def modificar_consecionario(request,nit):
    consecionario = get_object_or_404(Consecionario, pk=nit)
    formconsecionario = forms_consecionario(request.POST or None, instance=consecionario)
    if request.method == "POST":
        if formconsecionario.is_valid():
            formconsecionario.save()
            a = Consecionario.objects.all()
            return render(request,'venta/lista_consecionario.html',{'a':a})


    return render(request, "venta/modificar_consecionario.html", {"formconsecionario":formconsecionario})

def modificar_revision(request,id):
    revision = get_object_or_404(Revision, pk=id)
    formrevision = forms_revision(request.POST or None, instance=revision)
    if request.method == "POST":
        if formrevision.is_valid():
            formrevision.save()
            a = Revision.objects.all()
            return render(request,'venta/lista_revision.html',{'a':a})


    return render(request, "venta/modificar_revision.html", {"formrevision":formrevision})
