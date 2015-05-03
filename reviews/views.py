from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from reviews.models import Vehicle
from reviews.models import Review
from reviews.forms import SearchForm

def index(request):
	form = SearchForm()
	return render(request,'index.html',{'form': form,})
    #return render_to_response('index.html', context_instance = RequestContext(request))

def vehicle(request, year, make,model):
	#reviews = Vehicle.reviews.objects.all()
	results = Vehicle.objects.filter(Q(make__icontains=make) | Q(model__icontains=model) | Q(year__icontains=year))
	reviews = Review.objects.filter(Q(vehicle__make__icontains=make) | Q(vehicle__model__icontains=model) | Q(vehicle__year__icontains=year))
	a_year = results[0].year
	a_year = results[0].year
	a_make = results[0].make
	a_model = results[0].model

	return render(request,'carprofile.html', {'year': a_year, 'make': a_make, 'model': a_model, 'reviews': reviews})
	#return render_to_response('carprofile.html', {'year': a_year, 'make': a_make, 'model': a_model, 'reviews': reviews})

#def search(request):
#	results = BlogPost.objects.filter(Q(title__icontains=your_search_query) | Q(intro__icontains=your_search_query) | Q(content__icontains=your_search_query)).order_by('pub_date')

def search(request):
    if request.method == 'GET':
        form = SearchForm()
    else:
        # A POST request: Handle Form Upload
        form = SearchForm(request.POST) # Bind data from request.POST into a SearchForm
 
        # If data is valid, proceeds to search
        if form.is_valid():
            content = form.cleaned_data['search']
            contentList = content.split()

            results = Vehicle.objects.filter(Q(make__icontains=content) | Q(model__icontains=content) | Q(year__icontains=content))
            #created_at = form.cleaned_data['created_at']
            #post = m.Post.objects.create(content=content, created_at=created_at)
            #return HttpResponseRedirect('/result/')
            return render_to_response('search_result.html', {'results': results, 'content':content,})

    return render_to_response('search_result.html', {'form': form,})
 
    #return render(request, 'search_result.html', {'form': form,})

