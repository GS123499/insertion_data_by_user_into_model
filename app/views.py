from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Create your views here.
def insert_topic(request):
    if request.method=="POST":
        tn=request.POST['topic']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        return HttpResponse('insert_topic is done')


    return render(request,'insert_topic.html')

def insert_webpages(request):
    if request.method=="POST":
        wb=request.POST['webpage']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        W=Webpage.objects.get_or_create(topic_name=T)[0]
        



    return render(request,'insert_webpages.html')