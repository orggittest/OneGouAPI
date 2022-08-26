from django.urls import path

from .views import CategoryView, CatechildView, YgeatView, SearchCategory

app_name = 'fun'

urlpatterns = [
    path('category/',CategoryView.as_view(),name='category'),
    path('catchild/',CatechildView.as_view(),name='catchild'),
    path('ygeat/',YgeatView.as_view(),name='ygeat'),
    path('search/',SearchCategory.as_view(),name='search'),
]