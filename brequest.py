from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

# 拦截访问登陆之后才能访问的接口，判断是否登陆
class yan_login(MiddlewareMixin):

    def process_request(self, request):
        url_list = ['user/list/', 'user/address/', 'user/order/']
        url_list = []
        if request.path in url_list:
            if not request.session.get('user'):
                return JsonResponse({ 'msg': '用户未登陆'})
