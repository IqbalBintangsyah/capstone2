from multiprocessing import context
from urllib import response
from django.shortcuts import render
import requests
from django.http import HttpResponse
import static.lava.map as mp

def lahar(request):
    return render(request,'feature/lahar.html', {})

def lava(request):

    #Menjalankan program simulasi lava jika method POST (Submit button form diklik)
    if request.method == 'POST':
        volume = int(request.POST.get('Volume'))
        viskositas = request.POST.get('Viskositas')
        res = mp.main(volume, viskositas)
        print(volume, viskositas)
        return render(request, 'feature/lava.html', {
			"map": res
		})

    #Kalau web lava diakses dari link/sebelum submit button diklik, tidak ada gambar
    else:
        return render(request, 'feature/lava.html', {
			"map": None
		})

def piroklastik(request):
    return render(request,'feature/piroklastik.html', {})

def my_django_view(request):
    if request.method == 'GET':
        r = requests.get('https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-DIYogyakarta.xml', params=request.GET)
    return HttpResponse(r, content_type="text/xml")\
    