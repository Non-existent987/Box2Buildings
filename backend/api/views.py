from django.http import JsonResponse

def say_hello(request):
    # 返回一个 JSON 响应
    return JsonResponse({"message": "你好来自后端"})
