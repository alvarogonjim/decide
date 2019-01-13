from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404

from base import mods
from census.models import Census
from voting.models import Voting
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)
        admin_id = User.objects.filter(is_staff='t').first().id
        try:
            tk = Token.objects.filter(user_id=admin_id)[0].key
            r = mods.get('voting', params={'id': vid})
            c = mods.get('census', params={'voting_id': vid}, HTTP_AUTHORIZATION='Token ' + tk) 
            #Investigar otra forma de pasar Token
            context['voting'] = r[0]
            context['census'] = c
        except:
            raise Http404

        return context

