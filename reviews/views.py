from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q


def index(request):
    return render_to_response('index.html', context_instance = RequestContext(request))

def vehicle(request, year, make,model):
	#reviews = Vehicle.reviews.objects.all()
    return render_to_response('carprofile.html', context_instance = RequestContext(request))

#def search(request):
#	results = BlogPost.objects.filter(Q(title__icontains=your_search_query) | Q(intro__icontains=your_search_query) | Q(content__icontains=your_search_query)).order_by('pub_date')

