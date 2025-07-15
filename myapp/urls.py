
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path ('', TemplateView.as_view(template_name='home.html'), name='home'),
    path ('florida', TemplateView.as_view(template_name='florida.html'), name='florida'),
    path ('casique', TemplateView.as_view(template_name='casique.html'), name='casique'),
    path ('caracoli', TemplateView.as_view(template_name='caracoli.html'), name='caracoli'),
    
]