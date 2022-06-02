import chunk
from django.shortcuts import render

#project 
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os

def home(request):
    return render(request,'home/home.html', {})

def downloadfile(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'Original.jpg'
    filepath = base_dir + '/Files/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'), chunk_size), 
        content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;filename=%s" % filename
    return response