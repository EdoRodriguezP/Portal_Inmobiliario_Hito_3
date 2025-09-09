from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from .models import Inmueble



@method_decorator(login_required, name="dispatch")
class PerfilInmuebleListView(ListView):
    model = Inmueble
    template_name = "perfil/inmueble_list.html"
    context_object_name = "inmuebles"
    paginate_by = 10
    def get_queryset(self): return Inmueble.objects.filter(propietario=self.request.user).order_by("-creado")

