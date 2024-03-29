from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from reviews.models import Vehicle, ProfilePhoto, ReviewPhoto, VehiclePhoto
from reviews.models import Review
from reviews.forms import SearchForm, WriteReviewForm, AddVehicleForm, AddProfilePhotoForm
from django.contrib.auth.models import User

def index(request):
	# Landing page
	form = SearchForm()
	vehicles = Vehicle.objects.select_related().all()[:2]
	vehicles2 = Vehicle.objects.select_related().all()[2:4]
	vehicles3 = Vehicle.objects.select_related().all()[4:6]
	for vehicle in vehicles:
		vehicle.photo = VehiclePhoto.objects.select_related().filter(vehicle=vehicle)
	for vehicle in vehicles2:
		vehicle.photo = VehiclePhoto.objects.select_related().filter(vehicle=vehicle)
	for vehicle in vehicles3:
		vehicle.photo = VehiclePhoto.objects.select_related().filter(vehicle=vehicle)
	return render(request,'index.html',{'form': form, 'vehicles': vehicles,'vehicles2': vehicles2, 'vehicles3': vehicles3,})
    #return render_to_response('index.html', context_instance = RequestContext(request))

def vehicle(request, year, make,model):
	# View the car profile page
	#reviews = Vehicle.reviews.objects.all()
	results = Vehicle.objects.filter(Q(make__iexact=make) & Q(model__iexact=model) & Q(year__iexact=year))
	#results = Vehicle.objects.select_related().get(year=year, make = make, model = model)
	reviews = Review.objects.select_related().filter(vehicle=results)
	vehiclePhoto = VehiclePhoto.objects.select_related().filter(vehicle=results)
	form = WriteReviewForm()
	#reviews = Review.objects.filter(Q(vehicle__make__icontains=make) | Q(vehicle__model__icontains=model) | Q(vehicle__year__icontains=year))

	return render(request,'carprofile.html', {'year': year, 'make': make, 'model': model, 'reviews': reviews, 'form': form, 'vehiclePhoto': vehiclePhoto})
	#return render_to_response('carprofile.html', {'year': a_year, 'make': a_make, 'model': a_model, 'reviews': reviews})

def search(request):
	# Search the database for vehicle
    if request.method == 'GET':
        form = SearchForm()
    else:
        # A POST request: Handle Form Upload
        form = SearchForm(request.POST) # Bind data from request.POST into a SearchForm
 
        # If data is valid, proceeds to search
        if form.is_valid():
            content = form.cleaned_data['search']

            content = content.split()
            for term in content:
            	results = Vehicle.objects.filter(Q(make__icontains=term) | Q(model__icontains=term) | Q(year__icontains=term))
            return render(request,'search_result.html', {'results': results, 'content':content,})

    return render_to_response('search_result.html', {'form': form,})
 
    #return render(request, 'search_result.html', {'form': form,})



def add_vehicle(request):
    if request.method == 'GET':
        form = AddVehicleForm()
    else:
        # A POST request: Handle Form Upload
        form = AddVehicleForm(request.POST)

        if form.is_valid():
	        year = form.cleaned_data['year']
	        make = form.cleaned_data['make']
	        model = form.cleaned_data['model']

	        newCar = Vehicle(year=year, make=make, model=model)

	        newCar.save()
	        #reviews = Review.objects.filter(vehicle=Vehicle.objects.get(year=year, make = make, model = model))
	        #vehiclePhoto = VehiclePhoto.objects.select_related().filter(vehicle=Vehicle.objects.get(year=year, make = make, model = model))

	    	#return HttpResponseRedirect(reverse("reviews.views.vehicle"), {'year': year, 'make': make, 'model': model, 'reviews': reviews, 'form': form,})
	    	return render(request,'vehicle_added.html', {'year': year, 'make': make, 'model': model,})

    return render(request,'add_vehicle.html', {'form': form,})

def write_review(request, year, make, model):
	# Add a review to a vehicle
    if request.method == 'GET':
        form = WriteReviewForm()
    else:
        # A POST request: Handle Form Upload
        form = WriteReviewForm(request.POST)

        if form.is_valid():
	        title = form.cleaned_data['title']
	        body = form.cleaned_data['body']
	        #photos = form.cleaned_data['photo']
	        carToReview = Review(vehicle=Vehicle.objects.get(year=year, make = make, model = model))
	        

	        carToReview.title = title
	        carToReview.body = body
	        if request.user.is_authenticated():
	        	carToReview.author = request.user
	        carToReview.save()
	        #reviewPhoto = ReviewPhoto(review=carToReview,photo=photos)
	        #reviewPhoto.save()
	        reviews = Review.objects.filter(vehicle=Vehicle.objects.get(year=year, make = make, model = model))
	        vehiclePhoto = VehiclePhoto.objects.select_related().filter(vehicle=Vehicle.objects.get(year=year, make = make, model = model))
	    	#return HttpResponseRedirect(reverse("reviews.views.vehicle"), {'year': year, 'make': make, 'model': model, 'reviews': reviews, 'form': form,})
	    	return render(request,'carprofile.html', {'year': year, 'make': make, 'model': model, 'reviews': reviews, 'form': form,'vehiclePhoto': vehiclePhoto})

    return render_to_response('search_result.html', {'form': form,})


def my_profile(request):
	form = AddProfilePhotoForm()
	if request.user.is_authenticated():

		image = ProfilePhoto.objects.get(user=request.user)

		return render(request,'my_profile.html', {'username':request.user.username,'form':form, 'image':image})
	else:
		return render(request,'my_profile.html', {'username':username,'form':form,})


	


def upload_profile_photo(request,username):
    if request.method == 'GET':
        form = AddProfilePhotoForm()
    else:
        # A POST request: Handle Form Upload
        form = AddProfilePhotoForm(request.POST)

        if form.is_valid():
        	photo = form.cleaned_data['photo']

        	#if request.user.is_authenticated():
        	obj, created = ProfilePhoto.objects.update_or_create(user=request.user,photo=photo)
        	#profilePhoto.save()
        	image = ProfilePhoto.objects.filter(user=request.user)

	    	#return HttpResponseRedirect(reverse("reviews.views.vehicle"), {'year': year, 'make': make, 'model': model, 'reviews': reviews, 'form': form,})
	    	return render(request,'my_profile.html', {'username':username,'form':form, 'image':image})

    return render_to_response('search_result.html', {'form': form,})

