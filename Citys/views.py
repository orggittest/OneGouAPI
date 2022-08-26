import io
import json

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .api import CityModelsSerializers, CityAreaModelsSerializers

from .models import CityModels, CityAreaModels


class CityApi(View):
    def get(self, request):
        # city_letter_set = []
        # hot_city = CityModels.objects.filter(city_hot__gt=200).all()
        # ser = CityModelsSerializers(hot_city, many=True)
        # city_letter = CityModels.objects.values('city_letter').all()
        # for i in range(len(city_letter)):
        #     city_letter_set.append(city_letter[i]['city_letter'])
        # city_letter_set = set(city_letter_set)
        # city_name = sorted(city_letter_set)
        # print(city_name)
        # for j in range(len(city_name)):
        #     city = CityModels.objects.filter(city_letter=city_name[j]).all()
        #     ser_city = CityModelsSerializers(city, many=True)
        #     city_name[j] = [ser_city.data]
        # return JsonResponse({'data': {
        #     'hot_city': ser.data,
        #     'A': city_name[0][0],
        #     'B': city_name[1][0],
        #     'C': city_name[2][0],
        #     'D': city_name[3][0],
        #     'E': city_name[4][0],
        #     'F': city_name[5][0],
        #     'G': city_name[6][0],
        #     'H': city_name[7][0],
        #     'J': city_name[8][0],
        #     'K': city_name[9][0],
        #     'L': city_name[10][0],
        #     'M': city_name[11][0],
        #     'N': city_name[12][0],
        #     'P': city_name[13][0],
        #     'Q': city_name[14][0],
        #     'R': city_name[15][0],
        #     'S': city_name[16][0],
        #     'T': city_name[17][0],
        #     'W': city_name[18][0],
        #     'X': city_name[19][0],
        #     'Y': city_name[20][0],
        #     'Z': city_name[21][0],
        # }})
        city_all = CityModels.objects.all()
        ser = CityModelsSerializers(city_all, many=True)

        return JsonResponse({'data': ser.data})


class CityAreaApi(View):
    def get(self, request):
        a = request.GET.get('one_id', None)
        area_all = CityAreaModels.objects.filter(city_id=a).all()
        ser = CityAreaModelsSerializers(area_all, many=True)
        return JsonResponse({'data': ser.data})


class SetCity(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        area_id = json.loads(request.body, encoding='utf-8').get('area_id')
        city = CityAreaModels.objects.get(pk=area_id).city_id
        request.session['city'] = CityModelsSerializers(instance=city).data
        return JsonResponse({'status': 200})


