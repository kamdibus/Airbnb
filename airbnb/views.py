from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views import generic

from .models import Location

import sys

class IndexView(generic.ListView):
    template_name = 'airbnb/index.html'
    context_object_name = 'couple_of_locations'
    
    def get_queryset(self):
        return Location.objects.order_by('-precint_crime_rating')[:100]
    
class DetailView(generic.DetailView):
    model = Location
    template_name = 'airbnb/detail.html'
    
#class ListView(generic.ListView):
#    model = Location
#    paginate_by = 50
#    template_name = 'airbnb/list.html'
    
#    def get_queryset(self, **kwargs):
#        print("kwargs: ")
#        print(self.kwargs, file=sys.stderr)
#        query = kwargs['query']
#        arg = query[2:]
#        return Location.objects.filter(host_name=arg)
    
    #def get_context_data(self):#, **kwargs):
    #    #query = self.request.GET.get('q')
    #    context = Location.objects.order_by('-precint_crime_rating')[:100]
    #    return context
   
def index(request):
    couple_of_locations = Location.objects.order_by('-precint_crime_rating')[:10]
    template = loader.get_template('airbnb/index.html')
    context = {
        'couple_of_locations' : couple_of_locations,
        }
    return HttpResponse(template.render(context, request))
    
def detail(request, location_id):
    try:
        location = Location.objects.get(pk=location_id)
    except Location.DoesNotExist:
        raise Http404("Location does not exist")
    return render(request, 'airbnb/detail.html', {'location': location})
    
def list(request, query):
    results = Location.objects.filter(host_name=query)
    return render(request, 'airbnb/list.html', {'results': results})