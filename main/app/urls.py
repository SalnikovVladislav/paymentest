from django.urls import path
from .views import *


urlpatterns = [
    path('', item_list, name='item_list'),
    path('buy/<uuid:id>/', buy_item, name='buy_item'),
    path('item/<uuid:id>/', item_detail, name='item_detail'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]