from django.shortcuts import render ,HttpResponse
from app.models import *
from django.contrib import messages
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from app.models import*
from app.Resumes_Views_Admin import*
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    resume = Resume.objects.all().first()
    count = Resume.objects.all().count()
    posts = Resume.objects.all().order_by('-id')[:4:-1] # fetching all post objects from database
    paginator = Paginator(posts, 4) # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    totallist = page_obj.paginator.num_pages
    totalcount=paginator.count
    # page_list=[totallist+1 for totallist in range(totallist) ],
    
    context = {'segment': 'index' ,
               'resume':resume,
               'page_list': [totallist+1 for totallist in range(totallist) ],
               'page_obj': page_obj,
               'count':count,
               'totalcount':totalcount,
               
               }
    # context = {'segment': 'index' ,'resume':resume,'page_obj': page_obj}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

"""
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
   
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

"""
