from django.http import HttpResponse

def index(request):
    return HttpResponse("hello")
def about(request):
    return HttpResponse("helloabout")
def removepunc(request):
    return HttpResponse("removepunc")
def capfirst(request):
    return HttpResponse("capitalize")
def newlineremove(request):
    return HttpResponse("cremove")
def charcount(request):
    return HttpResponse("charcount")