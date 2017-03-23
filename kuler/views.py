#coding=utf-8
from django.shortcuts import render
import requests
import json
from django.shortcuts import render_to_response
from models import ColorPalette
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
# Create your views here.

def index(request):
    if not ColorPalette.objects.all().exists():
        getMostPopularColor()
    color_list = showTable()
    return render_to_response('index.html' , {'color_list': color_list})

def storeage(json_context):
    theme_list = json_context['themes']
    color_list = [json.dumps(item) for item in theme_list]
    #colorPalette = 
    for item in color_list:
        #color_palette = ColorPalette(attrs = item)
        ColorPalette.objects.create(attrs = item)
    #return res


# 1008 是Most_popular中最后一个包
def getMostPopularColor():
    params = {}
    params['filter'] = 'public'
    params['startIndex'] = 0
    params['maxNumber'] = 36
    params['sort'] = 'like_count'
    params['time'] = 'all'

    url = 'https://color.adobe.com/api/v2/themes'

    headers = {'x-api-key': '7810788A1CFDC3A717C58F96BC4DD8B4', 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
    r = requests.get(url , params = params , headers = headers)

    startIndex = 0
    print '------------- begin Crawl ---------------'
    while True:
        if startIndex != 1008:
            #startIndex += 36
            params['startIndex'] = startIndex
            r = requests.get(url , params = params , headers = headers)
            print r
            storeage(json.loads(r.text))
            startIndex += 36
        else:
            break
    print '----------- crawl Over -----------------'



def showTable():
    color_list = [item.attrs for item in ColorPalette.objects.all()]
    return color_list
    #return render_to_response('index.html' , {'color_list': color_list})
    #paginator = Paginator(color_list , 10)
