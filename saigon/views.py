from django.shortcuts import render
from django.http import HttpResponse
import pickle

# Create your views here.
chungcu = pickle.load(open('/media/cuongpc/DATA/workspace/python/web/django/bds/lnrgs/chungcu.sav', 'rb'))
gianha = pickle.load(open('/media/cuongpc/DATA/workspace/python/web/django/bds/lnrgs/nha.sav', 'rb'))


# def index(request):
#     return HttpResponse('dsad')
#
#
def add(request):
    return render(request, 'saigon/add.html')


def predict(request):
    if request.method == "POST":
        loai = request.POST['loai']
        dientich = int(request.POST['dientich'])
        sotang = int(request.POST['sotang'])
        sophongngu = int(request.POST['sophongngu'])
        sotoilet = int(request.POST['sotoilet'])
        noithat = int(request.POST['noithat'])
        if 15 < dientich and dientich < 300:
            if loai == '0':
                gia = chungcu.predict([[dientich, sophongngu, sotoilet, noithat]])
                gia = round(gia[0], 2)
                return HttpResponse(f'gia chung cu: {gia}')
                category='chung cu'
            else:
                gia = gianha.predict([[dientich, sotang, sophongngu, sotoilet, noithat]])
                gia = round(gia[0], 2)
                category='nhà riêng'
            context={'gia':gia,
                     'category':category
                     }
            return render(request, 'saigon/result.html',context=context)
        return HttpResponse('nhap lai')