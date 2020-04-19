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
def analyze(request):
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    print(djtext)
    print(removepun)
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")