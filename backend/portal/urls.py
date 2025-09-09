from django.urls import path
from .views import (
    HomeInmuebleListView,
    register_view, login_view, logout_view,
    PerfilView, PerfilEditView,
)
from .views_inmuebles_perfil import PerfilInmuebleListView
from . import views

urlpatterns = [
    path("", HomeInmuebleListView.as_view(), name="home"),

    # auth
    path("accounts/register/", register_view, name="register"),
    path("accounts/login/",    login_view,    name="login"),
    path("accounts/logout/",   logout_view,   name="logout"),

    # perfil
    path("perfil/", PerfilView.as_view(), name="perfil"),
    path("perfil/editar/", PerfilEditView.as_view(), name="perfil_editar"),
    path("perfil/inmuebles/",                 PerfilInmuebleListView.as_view(),  name="perfil_inmueble_list"),
]
