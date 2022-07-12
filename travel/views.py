from django.shortcuts import render
from rest_framework.views import APIView

from .serial import SOPTSeriailzer,tagsSeriailzer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from .models import SpotInfo,CommentTag

# Create your views here.
class SPOTView(APIView):
    def get(self, request):
        MM = SpotInfo.objects.all()
        Sdetial = SOPTSeriailzer(instance=MM, many=True)
        return HttpResponse(Sdetial.data)

class tagsView(APIView):
    def get(self, request):
        MM = CommentTag.objects.all()
        Sdetial = tagsSeriailzer(instance=MM, many=True)
        return HttpResponse(Sdetial.data)
class buttonView(APIView):
    def get(self,request):
        m=SpotInfo.objects.values('poiId')
        #url=f'https://m.ctrip.com/webapp/you/comment/district/4229-11.html?openapp=5&poiId={m}'
        return HttpResponse(m)