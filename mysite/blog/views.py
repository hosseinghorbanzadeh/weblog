from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from blog.models import *
from blog.forms import Newsletterform,Contactform
from blogpage.models import *
from django.contrib import messages

from django.http import HttpResponse


# Create your views here.

def index_view(request):
    posts=Post.objects.all()
    context={"posts":posts}
    return render(request,'website/index.html',context)
    #return render(request,'website/index.html')


def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = Contactform(request.POST)
        print('====================post===================================')
        if form.is_valid():
            form.instance.name="Unknown"
            form.save()
            messages.add_message(request, messages.SUCCESS, "Form saved successfully.")
        else:
            messages.error(request, 'The form was not saved successfully.!')
            print('===================The form was not saved successfully============================')

    form = Contactform()
    return render(request,'website/contact.html',{"form": form})
'''
def contact_view(request):
    if request.method == 'POST':
        print('Name : ')
        #print('Email : ',request.POST.get('email'))
    else:
        print("GET")
    form = Contactform()
    return render(request,'website/contact.html',{"form": form})
'''
#======================================================================

def elements_view(request):
    return render(request,'elements.html')


def newsletters_view(request):
    if request.method == 'POST':
        form= Newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def test(request):
    tmp_dict={}
    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Form saved successfully. !')
        else:
            return HttpResponse('The form was not saved successfully.!')

    form = Contactform()
    return render(request,'test.html',{"form": form})



#def coming_soon(request):
    #return HttpResponse("<h1 style='text-align:center; margin-top:50px;'>به زودی در دسترس خواهد بود</h1>")


def coming_soon(request):
    html = """
    <!DOCTYPE html>
    <html lang="fa">
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="این وبسایت به زودی در دسترس خواهد بود.">
        <meta name="keywords" content="وبلاگ, سایت در دست ساخت, به زودی">
        <meta name="author" content="Hossein Ghorbanzadeh">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>به زودی در دسترس خواهد بود</title>
    </head>
    <body>
        <h1 style='text-align:center; margin-top:50px;'>به زودی در دسترس خواهد بود</h1>
    </body>
    </html>
    """
    return HttpResponse(html)
