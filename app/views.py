from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.form import *

# Create your views here.
def fbv_string(request):
    return HttpResponse('<h1>This is the string from fbv_string')

class cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1>This is the string of cbv_string ')
    

def fbv_html(request):
    return render(request,'fbv_html.html')

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
    

def insert_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insertion by fbv is done')
    return render(request,'insert_fbv.html',d)

class insert_cbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'insert_cbv.html',d)
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert by Cbv is done')
        
class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'
