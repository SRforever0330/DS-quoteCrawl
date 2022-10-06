from django.shortcuts import render

# Create your views here.
from scrapy import cmdline
import os

from display.models import Quote


def index(request):
    # cmdline.execute('cd display'.split())
    # cmdline.execute('scrapy crawl quotes --nolog'.split())
    return render(request, 'index.html')


def spider_start(request):
    # os.system("cd display")
    # cmdline.execute('scrapy crawl quotes --nolog'.split())
    os.system("scrapy crawl quotes --nolog")
    data_list = Quote.objects.all()
    return render(request, 'index.html', {'data_list': data_list})
