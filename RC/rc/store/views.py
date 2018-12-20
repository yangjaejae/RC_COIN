from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Store, Category, Location, Photo
from .forms import StoreForm, PhotoForm

# Create your views here.

class StoreMyLV(ListView):
    paginate_by = 10
    context_object_name = 'stores'
    template_name = 'store/myStore_list.html'

    def get_queryset(self):
        queryset = Store.objects.filter(representative=self.request.user.id).order_by('-id')
        return queryset


class StoreDV(DetailView):
    model = Store
    context_object_name = 'store'
    template_name = 'store/myStore_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StoreDV, self).get_context_data(**kwargs)
        return context
        
class StorePV(ListView):
    paginate_by = 12
    context_object_name = 'photos'
    model = Photo
    template_name = 'store_list.html'

    # def store_list(request):
    #     print(1234, "##########################")
    #     return render(request, "store_list.html",({}))
    

class StoreDPV(DetailView):
    model = Photo
    context_object_name = 'photo'



def store_edit(request, store_id=None):
    user = request.user.pk

    if store_id:
        store = get_object_or_404(Store, pk=store_id)
        photo = get_object_or_404(Photo, store=store)
    else:
        store = Store()
        photo = Photo()

    if request.method == "POST":
        form = StoreForm(request.POST, instance=store)
        photo_form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            store = form.save(commit=False)
            store.store_id = store_id
            store.representative = User(user)
            store.status = "w"
            store.save()

            if photo_form.is_valid():
                photo = Photo(store=store, image=request.FILES['image'])
                photo.save()

        return redirect('store:myList')

    else:
        form = StoreForm(instance=store)
        photo_form = PhotoForm(instance=photo);
        category = Category.objects.all().order_by('id')
        location = Location.objects.all().order_by('id')
        return render(request, 'store/myStore_edit.html', dict(form=form, photo_form=photo_form, categorys=category, locations=location, store=store))


def store_remove(request, store_id=None):
    store = get_object_or_404(Store, pk=store_id)
    store.status = "d"
    store.save()
    return redirect('store:myList')


