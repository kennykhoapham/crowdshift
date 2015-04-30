from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from reviews.models import Vehicle

def index(request):
    return render_to_response('index.html', context_instance = RequestContext(request))

def vehicle(request, year, make,model):
	#reviews = Vehicle.reviews.objects.all()
	results = Vehicle.objects.filter(Q(make__icontains=make) | Q(model__icontains=model) | Q(year__icontains=year))
	a_year = results[0].year
	a_make = results[0].make
	a_model = results[0].model
	return render_to_response('carprofile.html', {'year': a_year, 'make': a_make, 'model': a_model})
#def search(request):
#	results = BlogPost.objects.filter(Q(title__icontains=your_search_query) | Q(intro__icontains=your_search_query) | Q(content__icontains=your_search_query)).order_by('pub_date')

