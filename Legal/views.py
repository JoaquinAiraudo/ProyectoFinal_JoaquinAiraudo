from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class Legal_view(TemplateView):
    tmpl = 'Legal/legal.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.tmpl, {'titulo':'INFORMACION LEGAL', 'contenido':'La utilización del sitio Web le otorga la condición de Usuario,\
         e implica la aceptación completa de todas las cláusulas y condiciones de uso incluidas en las páginas: - Aviso Legal - Política de Privacidad\
        Si no estuviera conforme con todas y cada una de estas cláusulas y condiciones absténgase de utilizar este sitio Web.\
        El acceso a este sitio Web no supone, en modo alguno, el inicio de una relación comercial con el Titular.\
        A través de este sitio Web, el Titular le facilita el acceso y la utilización de diversos contenidos que el Titular o sus colaboradores\
        han publicadon por medio de Internet. A tal efecto, usted está obligado y comprometido a NO utilizar cualquiera de los contenidos del sitio\
        Web con fines o efectos ilícitos, prohibidos en este Aviso Legal o por la legislación vigente, lesivos de los derechos e intereses de\
        terceros, o que de cualquier forma puedan dañar, inutilizar, sobrecargar, deteriorar o impedir la normal utilización de los contenidos, \
        los equipos informáticos o los documentos, archivos y toda clase de contenidos almacenados en cualquier equipo informático propios o\
        contratados por el Titular, de otros usuarios o de cualquier usuario de Internet.'})


class Privacity_view(TemplateView):
    tmpl = 'Legal/privacity.html'

    def get(self, request, *arg, **kwargs):
        return render(request, self.tmpl, {'titulo':'POLÍTICA DE PRIVACIDAD', 'contenido':'En el tratamiento de tus datos personales, el Titular aplicará los siguientes principios que se ajustan a las exigencias del nuevo reglamento europeo de protección de datos: \
            - Principio de licitud, lealtad y transparencia: El Titular siempre requerirá el consentimiento para el tratamiento de tus datos personales que puede ser para uno o varios fines específicos sobre los que te informará previamente con absoluta transparencia.\
            - Principio de minimización de datos: El Titular te solicitará solo los datos estrictamente necesarios para el fin o los fines que los solicita.\
            - Principio de limitación del plazo de conservación: Los datos se mantendrán durante el tiempo estrictamente necesario para el fin o los fines del tratamiento.\
            - El Titular te informará del plazo de conservación correspondiente según la finalidad. En el caso de suscripciones, el Titular revisará periódicamente las listas y eliminará aquellos registros inactivos durante un tiempo considerable.\
            - Principio de integridad y confidencialidad: Tus datos serán tratados de tal manera que su seguridad, confidencialidad e integridad esté garantizada. Debes saber que el Titular toma las precauciones necesarias para evitar el acceso no autorizado o uso indebido de los datos de sus usuarios por parte de terceros.'})