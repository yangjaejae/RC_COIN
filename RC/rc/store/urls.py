
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'store'

urlpatterns = [
    path('apply/', store_edit, name='add'),
    path('list/', StoreMyLV.as_view(), name='myList'),
    path('read/<int:pk>/',StoreDV.as_view(), name='read'),
    path('edit/<int:store_id>/', store_edit, name='edit'),
    path('delete/<int:store_id>/', store_remove, name='delete'),
    # path('view/', StorePV.as_view(), name='photoView'),
    # path('view/<int:store_id>/', StoreDPV.as_view(), name='detailPhotoView'),
    # path('history/', views.history, name='history'),

    path('store_list/', StorePV.as_view(), name='store_list'),
    path('store_list/filter/<int:loc>/',filteredStoresPV.as_view(), name='filteredStores')
    # path('view/<int:store_id>/', StoreDPV.as_view(), name='view_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
