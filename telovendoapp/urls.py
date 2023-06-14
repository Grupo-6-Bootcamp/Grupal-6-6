from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('formulario/', views.CrearProveedorView.as_view(),
         name='registro_proveedores'),
    path('proveedores/', views.ProveedoresView.as_view(), name='proveedores'),
    # Esta url en un futuro se debe cambiar por una redireccion en el backend, actualemente se utiliza para pruebas
    path('login/', views.LoginView.as_view(), name='login'),
    path('indexp/', views.IndexPageView.as_view(), name='homeprivado'),
    path('logout/', views.CerrarSesion.as_view(), name='logout'),
]
