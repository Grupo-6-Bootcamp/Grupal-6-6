
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from .form import FormularioProveedores, FormularioLogin
from .models import Proveedores
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    return render(request, "index.html")


def clients(request):
    clientes = [
        {
            "id": 1,
            "nombre": "Diego",
            "apellido": "Herrera",
            "email": "diego.herrer@email.cl",
            "edad": 25,
            "telefono": "31245698"
        },
        {
            "id": 2,
            "nombre": "Nicolas",
            "apellido": "Castro",
            "email": "nico.castro@email.cl",
            "edad": 28,
            "telefono": "31245864"
        },
        {
            "id": 3,
            "nombre": "Carolina",
            "apellido": "Vargas",
            "email": "caro.vargas@email.cl",
            "edad": 35,
            "telefono": "31663864"
        },
        {
            "id": 4,
            "nombre": "Valentina",
            "apellido": "Fernandez",
            "email": "vale.fer@email.cl",
            "edad": 30,
            "telefono": "2654815"
        },
        {
            "id": 5,
            "nombre": "Sebastian",
            "apellido": "Lopez",
            "email": "seba.lopez@mail.cl",
            "edad": 28,
            "telefono": "91856864"
        }
    ]
    return render(request, "clients.html", {"clientes": clientes})

# class FormView(TemplateView):
#     template_name = "formulario.html"
#     def get_context_data(self, **kwargs):
#         context = super(FormView, self).get_context_data(**kwargs)
#         context['form'] = FormularioProveedores()
#         return context

#     def post(self, request, *args, **kwargs):
#         form = FormularioProveedores(request.POST)
#         if form.is_valid():
#             return HttpResponse("Formulario valido")
#         else:
#             return render(request, "formulario.html", {"form": form})


class CrearProveedorView(View):
    template_name = "formulario.html"

    def get(self, request):
        form = FormularioProveedores()
        context = {'form': form}
        return render(request, 'formulario.html', context)

    def post(self, request):
        form = FormularioProveedores(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
        else:
            context = {'form': form}
            return render(request, 'formulario.html', context)


class ProveedoresView(TemplateView):
    template_name = "proveedores.html"

    def get(self, request):
        proveedores = Proveedores.objects.all()
        context = {"proveedores": proveedores}
        return render(request, "proveedores.html", context)


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        context = {'formulario_login': FormularioLogin()}
        return render(request, "login.html", context)

    def post(self, request):
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if usuario is not None:
            login(request, usuario)
            return redirect('homeprivado')
        else:
            context = {"error": "Usuario no encontrado",
                       'formulario_login': FormularioLogin()}
            return render(request, 'login.html', context)


@method_decorator(login_required, name='dispatch')
class IndexPageView(TemplateView):
    template_name = "indexp.html"

    def get(self, request):
        return render(request, "indexp.html")

    def post(self, request):
        return render(request, "indexp.html")


class CerrarSesion(View):
    def get(self, request):
        logout(request)
        return redirect('index')
