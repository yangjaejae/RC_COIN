from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
from .models import Store, Category, Location
from .forms import StoreForm


# Create your views here.

class StoreLV(ListView):
    paginate_by = 10
    context_object_name = 'stores'

    def get_queryset(self):
        queryset = Store.objects.filter(representative=self.request.user.id).order_by('-id')
        return queryset


class StoreDV(DetailView):
    model = Store
    context_object_name = 'store'

    def get_context_data(self, **kwargs):
        context = super(StoreDV, self).get_context_data(**kwargs)
        return context


def store_edit(request, store_id=None):
    user = request.user.pk

    if store_id:
        store = get_object_or_404(Store, pk=store_id)
    else:
        store = Store()

    if request.method == "POST":
        form = StoreForm(request.POST, instance=store)

        if form.is_valid():
            store = form.save(commit=False)
            store.store_id = store_id
            store.representative = User(user)
            store.status = "w"
            store.save()
        return redirect('store:myList')

    else:
        form = StoreForm(instance=store)
        category = Category.objects.all().order_by('id')
        location = Location.objects.all().order_by('id')
        return render(request, 'store/store_edit.html', dict(form=form, store=store, categorys=category, locations=location))


def store_remove(request, store_id=None):
    store = get_object_or_404(Store, pk=store_id)
    store.status = "d"
    store.save()
    return redirect('store:myList')
