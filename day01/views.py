from django.http import JsonResponse


def test_cors(rqequest):
    return JsonResponse({'msg':'CORS is ok'})