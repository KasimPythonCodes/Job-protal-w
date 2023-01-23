from django.shortcuts import render ,HttpResponse ,redirect
from django.http import HttpResponse , HttpResponseNotFound,HttpResponseRedirect
from app.models import *
from django.contrib import messages

from django.core.paginator import Paginator
from pathlib import Path
import os
import datetime
from django import forms
import csv
from io import BytesIO
from django.template.loader import get_template
from django.http import HttpResponse, Http404
from django.core.files.storage import FileSystemStorage
from pathlib import Path
import os
from django.http import FileResponse
from django.conf import settings 
from django.conf.urls.static import static
from django.core.paginator import Paginator
from app.forms import*


# Create your views here.





"""
       Start Admin Panel Function
"""


def  view_resume(request):
    show_resume = Resume.objects.all()[::-1]
    paginator = Paginator(show_resume , 10)
    page_number = request.GET.get('page')
    show_resume = paginator.get_page(page_number)
    totallist = show_resume.paginator.num_pages
    # page_list = [totallist+1 for totallist in range(totallist) ],
    # getting the desired page number from url
   
    return render(request , 'home/tables.html' , {'show_resume':show_resume, 'page_list':[totallist+1 for totallist in range(totallist) ],
 })


def USER_RESUME_POST(request):
    pass



def ResumeDelete(request ,id):
    Resumeuser = Resume.objects.get(id=id) 
    Resumeuser.delete()
    messages.success(request , "Record are Successfully Deleted")  
    return HttpResponseRedirect('/')

def Resume_Views_Delete(request ,id):
    Resumeuser = Resume.objects.get(id=id) 
    Resumeuser.delete()
    messages.success(request , "Record are Successfully Deleted")  
    return HttpResponseRedirect('/show-resume/') 

  



def ADD_POST(request):
    if request.method == 'POST':
        form = POST_VIEWS_FORM(request.POST )
        if form.is_valid():
            job_profile = form.cleaned_data['job_profile']
            company_name = form.cleaned_data['company_name']
            job_location = form.cleaned_data['job_location']
            min_salary = form.cleaned_data['min_salary']
            max_salary = form.cleaned_data['max_salary']
            Vacancy = form.cleaned_data['Vacancy']
            job_description = form.cleaned_data['job_description']
            # job_skill = form.cleaned_data['job_skill']
            # job_experience = form.cleaned_data['job_experience']
            package = form.cleaned_data['package']
            dataip=request.META.get('REMOTE_ADDR')
            
            # job_profiles=job_profile.replace(" ", "")
            # print(job_description,job_location,job_profile,min_salary,max_salary,Vacancy,package)
            
            

            """ 
            job_profile = request.POST['job_profile']
            company_name = request.POST['company_name']
            job_location = request.POST['job_location']
            min_salary = request.POST['min_salary']
            max_salary = request.POST['max_salary']
            Vacancy = request.POST['Vacancy']
            job_description = request.POST['job_description']
            job_skill = request.POST['job_skill']
            job_experience = request.POST['job_experience']
            package = request.POST['package']
            
            """
            jobpost=job_post(job_profile = job_profile ,company_name=company_name
                          ,job_location=job_location ,min_salary=min_salary,
                          max_salary=max_salary,Vacancy=Vacancy ,job_description=job_description
                          ,package=package )
            jobpost.save()
            messages.success(request , str(f'{job_profile}' + "  - " + "   " + "Job vacancy successfully Post"))
            return redirect('/addpost/')
    else:
        form =POST_VIEWS_FORM()
    return render(request , 'home/addpost.html' , {'form':form})        
        
   
def VIEWS_POST(request):
    view = job_post.objects.all()[::-1]
    paginator = Paginator(view , 10)
    page_number = request.GET.get('page')
    view = paginator.get_page(page_number)
    totallist = view.paginator.num_pages
    return render(request , 'home/view_post.html' , {'view':view,'page_list':[totallist+1 for totallist in range(totallist) ],})
         

def UPDATE_POST(request ,id):
    edits = job_post.objects.filter(id = id)
    context = {
        'edits':edits
    }
    return render(request , 'home/view_post.html' , context)


def EDIT_POST_DATA(request,id):
    instance = job_post.objects.get(id=id)
    form = POST_VIEWS_FORM(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        messages.success(request , "Post are Successfully Updated")  
        return redirect('/post-view/')
    return render(request, 'home/update_post.html', {'form': form})  
        
def DELETE_POST(request,id):
    delvalue=job_post.objects.get(id=id)
    delvalue.delete()
    messages.success(request , "Post are Successfully Deleted")  
    return HttpResponseRedirect('/post-view/') 

         
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q 

@csrf_exempt

def SEARCH_BAR_ACTIVATE_RESUME(request):
    # return HttpResponse("this is search")
    if request.method ==  "GET":
        searched = request.GET.get('query')
        if searched:
            # show = Resume.objects.all().filter(__icontains=searched)
            show=Resume.objects.filter(Q(first_name__icontains=searched)|Q(last_name__icontains=searched)|
                                       Q(work_expriance__icontains=searched)|Q(job_type__icontains=searched)|
                                       Q(email__icontains=searched)|Q(job_profile__icontains=searched)|
                                       Q(remote_type__icontains=searched)
                                       )
            return render(request ,'home/search.html' , {'show':show , 'searched':searched})
       
        else:
            print("NO Item informations")
            return render(request ,'home/search.html' , {})


def SEARCH_BAR_ACTIVATE_VIEWS_POST(request):
    # return HttpResponse("this is search")
    if request.method ==  "GET":
        searched = request.GET.get('query')
        
        
        if searched:
            # show = Resume.objects.all().filter(__icontains=searched) 
            show=job_post.objects.filter(Q(job_profile__icontains=searched)|Q(company_name__icontains=searched)|
                                       Q(job_location__icontains=searched)
                                       )
            return render(request ,'home/post_search.html' , {'show':show , 'searched':searched})
        else:
            print("NO Item informations")
            return render(request ,'home/post_search.html' , {})
            










            # return r

# def SEARCH_BAR_ACTIVATE(request):
#     # return HttpResponse("this is search")
#     if request.method ==  "POST":
#         searched = request.POST.get('query')
#         if searched:
#             show= Resume.objects.filter(first_name__icontains=searched)
#             return render(request ,'home/search.html' , {'show':show , 'searched':searched})
#         else:
#             print("NO Item informations")
#             return render(request ,'home/search.html' , {})
#             # return render(request, 'AGENT/add_installment1.html',{'searched':searched,'venues':venues})            

         


"""
        End Admin Panel Function
  
"""        


    
# def Download_all(request,pdfSlug):
#     a = Resume.objects.get(id=pdfSlug)
#     # sending the page object to index.html
#     with open(str(a.doc.path), 'rb') as pdf:
#         response = HttpResponse(pdf, content_type='application/pdf')
#         response['Content-Disposition'] = 'filename=The Wolf Work Morden Template .pdf'
#         return response
       
       
# def Download_all(request,pdfSlug):
#     a = Resume.objects.get(id=pdfSlug)
#     # sending the page object to index.html
#     with open(str(a.doc.path), 'rb') as pdf:
#         response = HttpResponse(pdf.head(), content_type='application/pdf')
#         response['Content-Disposition'] = 'filename=The Wolf Work Morden Template .pdf'
#         return response

      
# import json       
# def Download_all_doc(request,pdfSlug):
#     a = Resume.objects.get(id=pdfSlug)
#     # sending the page object to index.html
#     data = open(a.doc, "rb").read() #//doc.name is youre filefield from your model
#     return HttpResponse(data, content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
  
    # with open(str(a.doc.path), 'rb') as pdf:
    #     response = HttpResponse(pdf, content_type='application/docx')
    #     response['Content-Disposition'] = 'filename=The Wolf Work Morden Template .doc'
    #     return response 

            
   






# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# p = Paginator(list_of_objects, no_of_objects_per_page)

"""
class MyForm(forms.ModelForm):

    def clean_file(self):
        file = self.cleaned_data['file']
        try:
            if file:
                file_type = file.content_type.split('/')[0]
                print (file_type)

                if len(file.name.split('.')) == 1:
                    raise forms.ValidationError(_('File type is not supported'))

                if file_type in settings.TASK_UPLOAD_FILE_TYPES:
                    if file._size > settings.TASK_UPLOAD_FILE_MAX_SIZE:
                        raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.TASK_UPLOAD_FILE_MAX_SIZE), filesizeformat(file._size)))
                else:
                    raise forms.ValidationError(_('File type is not supported'))
        except:
            pass

        return file

"""
# def Download_Resume(request):
#     a = Resume.objects.all()
#     for i in a:
#     # sending the page object to index.html
#         with open(str(i.doc.path), 'rb') as pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             response['Content-Disposition'] = 'filename=The Wolf Work Morden Template .pdf'
#             return response


# def render_to_pdf(template_src , content_dict = {}):
#     template = get_template(template_src)
#     html = template.render(content_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8559-1")),result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue() , content_type='application/pdf')
#     return None

"""
def Download_all(request):
    fs=FileSystemStorage()
    # filename = os.path.join(BASE_DIR / 'media')
    path = os.path.join(settings.MEDIA_ROOT )#4
    response = FileResponse(open(path, 'rb'), content_type="application/pdf")
    response["Content-Disposition"] = "filename={}".format(path)
    return response
    # filename = str(datetime.datetime.now())
    # filename ='kasimsaifi_resume.pdf'
    
    # assert os.path.isfile(filename)
    # with open(path, "r") as f:
    # if fs.exists(filename):
    #     with fs.open(filename , 'r') as pdf :
    #         response = HttpResponse(pdf ,content_type = 'application/pdf')
    #         response['Content-Disposition'] = 'inline; filename = "filename" '
    #         # resume_list = Resume.objects.filter(id=id)
    #         # for i in resume_list:
    #         #     i.doc
    #         return response 
    # else:
    #     return HttpResponseNotFound("The request pdf doen't exixst")
   
"""  

"""
def Download_all(request,id):
    response = HttpResponse(content_type = 'text/csv')
    #response['Content-Disposition'] = 'attachment; filename="Approve Po.csv"'
    response['Content-Disposition'] = 'attachment; filename = Resume Details'+ str(datetime.datetime.now())+'.csv'
    resume_list = Resume.objects.filter(id=id)
    writer = csv.writer(response)
    # writer.writerow(['User Id', 'Ref ID', 'User Name', 'Amount'])
    writer.writerow(['Doc'])
    for approve in resume_list:
        print(approve)
        writer.writerow(
                [
				approve.doc, 
                ])
           
        return response
"""
    
"""
import PyPDF2

# Download_all

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


def Download_all(request,id):

    # Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()

        # Create the PDF object, using the buffer as its "file."
        p = canvas.Canvas(buffer)
        resume_list = Resume.objects.filter(id=id)
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        for i in resume_list:
            p.drawString(100, 100, 'i')

            # Close the PDF object cleanly, and we're done.
            p.showPage()
            p.save()

            # FileResponse sets the Content-Disposition header so that browsers
            # present the option to save the file.
            buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=i.doc)    
        
"""        