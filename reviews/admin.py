from django.contrib import admin
from reviews.models import Vehicle
from reviews.models import Review, ProfilePhoto, VehiclePhoto, ReviewPhoto

admin.site.register(Vehicle)
admin.site.register(Review)
admin.site.register(ProfilePhoto)
admin.site.register(VehiclePhoto)
admin.site.register(ReviewPhoto)
# Register your models here.
