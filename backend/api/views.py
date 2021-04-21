import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# connect to our Redis instance
redis_instance = redis.Redis()


@api_view(['GET'])
def search_stocks_by_name(request, *args, **kwargs):
    items = {}
    stock_name = request.query_params["search"].upper() + "*"
    for key in redis_instance.keys(stock_name):
        temp = {}
        for k, v in redis_instance.hgetall(key).items():
            temp[k.decode("utf-8")] = v.decode("utf-8")
        items[key.decode("utf-8")] = temp

    return Response(items, status=200)
