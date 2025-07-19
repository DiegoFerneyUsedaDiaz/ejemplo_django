
from django.urls import path
from django.views.generic import TemplateView
from .views import lista_centros_comerciales
from myapp import views

urlpatterns = [
    path ('', TemplateView.as_view(template_name='home.html'), name='home'),
    path ('florida', TemplateView.as_view(template_name='florida.html'), name='florida'),
    path ('casique', TemplateView.as_view(template_name='casique.html'), name='casique'),
    path ('caracoli', TemplateView.as_view(template_name='caracoli.html'), name='caracoli'),
    path ('megamall', TemplateView.as_view(template_name='megamall.html'), name='megamall'),
    path ('centros_comerciales', views.lista_centros_comerciales, name='lista_centros_comerciales'),
    path('tiendas', views.lista_centros_tiendas, name='lista_centros_tiendas'),
    path('cc/<str:name_cc>', views.vista_centros_comercial, name='vista_centros_comercial' ),
]