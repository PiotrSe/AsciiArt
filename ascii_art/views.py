from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from ascii_art.Tools.AsciiArt import Ascii_art
import json
from ascii_art.Tools.AsciiArt.Ascii_art import Ascii_art
from ascii_art.Tools.AsciiArt.Animated_ascii_art import Animated_ascii_art
# Create your views here.

def ascii(request):
    return render(request,'ascii.html')


def animated_ascii(request):
    return render(request,'animated_ascii.html')

#created for web site - return href link to ascii art file

@csrf_exempt
def do_animated_ascii_art(request):
    
    try:
        uploaded_file = request.FILES['file']
        print(request.FILES['file'])
        
        print("image width:")
        image_width = int(request.POST['image_width'])
        print(image_width)
        
        if image_width  > 270 or int(image_width) < 50:
        
             return HttpResponse("Animation width value out of range.Enter 50 - 270")

    except Exception as e:
        print(str(e))
        return HttpResponse("no file selected")
      
    animated_ascii_art = Animated_ascii_art()
    context = animated_ascii_art.do_animated_ascii_art(uploaded_file,image_width)
    
    if context['animated_ascii_file']!= None: # image file correct
        link = '<a href=/%s>Data ready - click</a>' % context['animated_ascii_file']
        #link = context['filepath']
        
    else: # file incorrect return err
        link = '<b>' + context['message'] + '</b>'

    #zwracamy link do pliku z ascii
    result = json.dumps(link)
    return HttpResponse(result)


@csrf_exempt
def do_ascii_art_web(request):

    try:
        uploaded_file = request.FILES['file']
        print(request.FILES['file'])
        
        print("image width:")
        image_width = int(request.POST['image_width'])
        print(image_width)
        
        if image_width  > 270 or int(image_width) < 50:
        
             return HttpResponse("Image width value out of range.Enter 50 - 270")
        
    except Exception as e:
        print(str(e))
        return HttpResponse("no file selected")
      
    ascii_art = Ascii_art()
    context = ascii_art.do_ascii_art(uploaded_file,image_width)
    if context['filepath']!= None: # image file correct
        link = '<a href=/%s>Data ready - click</a>' % context['filepath']
        #link = context['filepath']
        
    else: # file incorrect return err
        link = '<b>' + context['ascii'] + '</b>'

    #zwracamy link do pliku z ascii
    result = json.dumps(link)
    return HttpResponse(result)



# return plain path to asci art file
@csrf_exempt
def do_ascii_art(request):

    try:
        uploaded_file = request.FILES['file']
        print(request.FILES['file'])
        
        image_width = int(request.POST['image_width'])
        
        print("image_width:")
        print(image_width)
        #image_width = 60
        
        if image_width  > 270 or int(image_width) < 50:
        
             return HttpResponse("Image width value out of range.Enter 50 - 270")

        
    except Exception as e:
        print(str(e))
        return HttpResponse("no file selected")
      
    ascii_art = Ascii_art()
    context = ascii_art.do_ascii_art(uploaded_file,image_width)
    if context['filepath']!= None: # image file correct
        out_file = context['filepath']
        
    else: # file incorrect return err
        out_file = '<b>' + context['ascii'] + '</b>'

    #zwracamy link do pliku z ascii
    result = json.dumps(out_file)
    return HttpResponse(result)
