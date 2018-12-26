from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from libs.decorators import json_view
from dashboard import documents


@json_view
def index(request):
    docs_count = documents.Actions.objects().count()
    return {
        'status': 'ok',
        'results': 'hello from json',
        'count': docs_count
    }
