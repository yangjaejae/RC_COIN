from django.contrib import admin
from .models import Store, Location, Category

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
    model = Store
    verbose_name_plural = 'store'

class LocationAdmin(admin.ModelAdmin):
    model = Location
    verbose_name_plural = 'location'

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    verbose_name_plural = 'category'

admin.site.register(Store, StoreAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Category, CategoryAdmin)