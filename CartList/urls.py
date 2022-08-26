from django.urls import path
from .views import *

app_name = 'cartapp'
urlpatterns = [
    path('getcart/', GetCartView.as_view(), name='get_cart'),
    path('addsuborder/', AddCartView.as_view(), name='add_cart'),
    path('orderdown/', OrderDownView.as_view(), name='order_down'),
    path('sum/', CartSumView.as_view(), name='sum'),
]
