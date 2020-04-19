from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'pk','place':'mars'}
    return render(request,'index.html',params)
    #return HttpResponse("hello")
def about(request):
    return render(request, 'about.html')
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
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount','off')
    #Check which checkbox is on
    purpose = ""
    count = 0
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        #params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed
        purpose = purpose + "Removepun "
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        #params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyze.html', params)
        djtext = analyzed
        purpose = purpose + "Fullcaps "
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        #params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        #return render(request, 'analyze.html', params)
        djtext = analyzed
        purpose = purpose + "Extra_space_rem "
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        djtext = analyzed
        purpose = purpose + "Newlineremove"
    if (charcount == "on"):
        analyzed = ""
        for char in djtext:
            if char != " ":
                count = count+1
        purpose = purpose + "charcount"  
    if not(purpose == "" ):
        if not(count == 0):
            params = {'purpose': purpose, 'analyzed_text': djtext,'count':count}
        # Analyze the text
        else:
            params = {'purpose': purpose, 'analyzed_text': djtext}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Select any operation")