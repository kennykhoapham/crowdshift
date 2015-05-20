from django.contrib import admin
from reviews.models import Vehicle
from reviews.models import Review, ProfilePhoto

admin.site.register(Vehicle)
admin.site.register(Review)
admin.site.register(ProfilePhoto)
# Register your models here.
