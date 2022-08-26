from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


from Funy.models import CategoryModel,YgeatModel
from .api import CategoryModelSerializers,YgeatModelSerializers

class CategoryView(View):
    def get(self,request):
        datas = CategoryModel.objects.values('id','name').filter(father_id='00000000-0000-0000-0000-000000000000').all()
        ser = CategoryModelSerializers(datas,many=True)

        return JsonResponse({
            'data':ser.data,
            'status': 200
        })

class CatechildView(View):
    def get(self,request):
        f_id = request.GET.get('id',None)
        if f_id:
            datas = CategoryModel.objects.filter(father_id=f_id).all()
        else:
            datas = CategoryModel.objects.filter(father_id='ccd5a8ef-66ca-48d2-962c-613d23500cf9')
        ser = CategoryModelSerializers(datas, many=True)
        return JsonResponse({
            'data': ser.data,
            'status':200
        })

class YgeatView(View):
    def get(self,request):
        datas = YgeatModel.objects.all()
        ser = YgeatModelSerializers(datas,many=True)
        return JsonResponse({
            'data':ser.data,
            'status': 200
        })


class SearchCategory(View):
    def get(self, request):
        name = request.GET.get('info', None)
        id = CategoryModel.objects.filter(name=name).first()
        if id:
            datas = CategoryModel.objects.filter(father_id=id).all()
            cateinfo = CategoryModelSerializers(datas,many=True)
            return JsonResponse({
                'data':cateinfo.data,
                'status': 200
            })
        else:
            return JsonResponse({
                'mesg':'未查询到对应商品',
                'status': 400
            })