from django.urls import path

from .views import CityApi, CityAreaApi, SetCity

app_name = 'city'


urlpatterns = [
    # path('get_city/',CityApi.as_view(),name='city'),
    path('all/',CityApi.as_view(),name='city'),
    path('area/',CityAreaApi.as_view(),name='area'),
    path('set_city/', SetCity.as_view(), name='set_city')
]