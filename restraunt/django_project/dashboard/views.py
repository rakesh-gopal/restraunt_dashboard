from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from libs.decorators import json_view


@json_view
def index(request):
    return {
        'status': 'ok',
        'results': 'hello from json'
    }
