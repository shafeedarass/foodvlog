from django.shortcuts import render
from .models import place,news
# Create your views here.
def index(request):
    obj=place.objects.all()
    objt=news.objects.all()
    return render(request,'index.html',{'results': obj,'new':objt})