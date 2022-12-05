# I have created this website
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    cap_first = request.POST.get('cap_first', 'off')
    remove_new_line = request.POST.get('remove_new_line', 'off')
    remove_space = request.POST.get('remove_space', 'off')
    char_counter = request.POST.get('char_counter', 'off')

    analyzed = ''
    purpose = ''
    if removepunc == 'on':
        punctuations = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose = purpose + 'Remove Punctuations '

        djtext = analyzed

    if uppercase == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char

        purpose = purpose + 'Convert to uppercase '

        djtext = analyzed.upper()
    if cap_first == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char
        purpose = purpose + 'First letter capital '
        djtext = analyzed.capitalize()
    if remove_new_line == 'on':
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        purpose = purpose + 'Remove New Line '
        djtext = analyzed
    if remove_space == 'on':
        text = ''
        for char in djtext:
            if char in djtext:
                text = text + char.replace(" ", "")
        purpose = purpose + 'Remove Space '
        djtext = text
    if char_counter == 'on':
        analyzed = ''

        for char in djtext:
            analyzed = analyzed + char
        purpose = purpose + 'Remove Space'
        djtext = len(analyzed)

    params = {'purpose': purpose, 'analyzed_text': djtext}
    if removepunc == 'on' or uppercase == 'on' or cap_first == 'on' or remove_new_line == 'on' or char_counter == 'on' or remove_space == 'on':
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

def aboutus(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
