from django.forms import ModelForm

from .models import Location, Category, Store

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['loc']

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['domain']

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = [
            'name', 'corporate_number', 'category', 'location', 'address', 'phone_number', 'url',
                  'opening_hour', 'opening_minute', 'closing_hour', 'closing_minute', 'description'
        ]
