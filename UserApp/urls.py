from django.urls import path
from .tool import new_img_code
from UserApp.views import UserAPIView, AddressAPIView, UserOrder, UserCart

app_name = 'user_app'

urlpatterns = [
    path('list/',UserAPIView.as_view(), name='list'),
    path('yzm/', new_img_code, name='yzm'),
    path('address/', AddressAPIView.as_view(), name='address'),
    path('order/', UserOrder.as_view(), name='order'),
    path('cart/', UserCart.as_view(), name='cart')
]

