"""proyecto_Simulacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto_Simulacion import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('HolaMundo/',views.HolaMundo),
    path('AdiosMundo/',views.AdiosMundo),
    path('Fecha/',views.dameFecha),
    path('Inicio/',views.Inicio),

    path('cuadrados_Medios/',views.cuadrados_Medios),
    path('cuadradosMedios/',views.cuadradosMedios),
    path('congruencial_Lineal/',views.congruencial_Lineal),
    path('congruencialLineal/',views.congruencialLineal),
    path('transformada_Inversa/',views.transformada_Inversa),
    path('transformadaInversa/',views.transformadaInversa),
    path('promedio_Movil/',views.promedio_Movil),
    path('promedioMovil/',views.promedioMovil),
    path('alisamiento_Exponencial/',views.alisamiento_Exponencial),
    path('alisamientoExponencial/',views.alisamientoExponencial),
    path('regresion_Lineal/',views.regresion_Lineal),
    path('regresionLineal/',views.regresionLineal),
    path('regresion_No_Lineal/',views.regresion_No_Lineal),
    path('regresionNoLineal/',views.regresionNoLineal),
    path('linea_De_Espera/',views.linea_De_Espera),
    path('lineaDeEspera/',views.lineaDeEspera),
    path('linea_De_Espera_Montecarlo/',views.linea_De_Espera_Montecarlo),
    path('lineaDeEsperaMontecarlo/',views.lineaDeEsperaMontecarlo),

    path('Edades/<int:edad>/<int:anio>',views.calcula_Edad),    
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
