from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'pk','place':'mars'}
    return render(request,'index.html',params)
    #return HttpResponse("hello")
def about(request):
    return HttpResponse("helloabout")
def removepunc(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse("removepunc <a href='/about'>back</a>")
def capfirst(request):
    return HttpResponse("capitalize")
def newlineremove(request):
    return HttpResponse("cremove")
def charcount(request):
    return HttpResponse("charcount")