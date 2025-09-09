from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import Inmueble, SolicitudArriendo
from .form import RegisterForm, LoginForm, PerfilUserForm

# HOME: lista de inmuebles
class HomeInmuebleListView(ListView):
    model = Inmueble
    template_name = "web/home.html"
    context_object_name = "inmuebles"
    paginate_by = 12
    ordering = ["-creado"]

# AUTH
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cuenta creada correctamente.")
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "registration/register.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, "Has iniciado sesión.")
        return redirect("home")
    return render(request, "registration/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect("login")

# PERFIL (muestra enviadas/recibidas y botón a CRUD de inmuebles)
class PerfilView(TemplateView):
    template_name = "usuarios/perfil.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        u = self.request.user
        ctx["enviadas"] = u.solicitudes_enviadas.select_related("inmueble", "inmueble__comuna").order_by("-creado")
        ctx["recibidas"] = (SolicitudArriendo.objects
                            .filter(inmueble__propietario=u)
                            .select_related("inmueble", "inmueble__comuna", "arrendatario")
                            .order_by("-creado"))
        return ctx

class PerfilEditView(UpdateView):
    form_class = PerfilUserForm
    template_name = "usuarios/perfil.html"
    success_url = reverse_lazy("perfil")
    def get_object(self, queryset=None): return self.request.user

