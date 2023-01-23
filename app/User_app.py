from django.shortcuts import render ,HttpResponse ,redirect
from django.http import HttpResponse , HttpResponseNotFound,HttpResponseRedirect

from app.models import *
from django.contrib import messages
from django.core.validators import FileExtensionValidator

# avatar = models.ImageField(upload_to = "image/avatar", validators=[FileExtensionValidator(allowed_extensions=['png','jpg'])])
   

"""
    Strat User/Employee/Student/Other Panel Function
"""
import os


def USER_RESUME_POST(request):
    if request.method == 'POST':
        myfile = request.FILES.get('myfile')
        content_types=['application/pdf']
        if myfile == content_types:
        # filename, ext = os.path.splitext(myfile)[-1].lower()
        # if ext== '.pdf' or '.doc' or '.docx':
            ProfileAvatarFile(avatar=myfile).save()
        else:
                print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")    
        return render(request , "Resume/resume.html")
    return render(request , "Resume/resume.html")


def FileFunction(request):
    if request.method == 'GET':
        myfile = request.FILES.get('myfile')
        filepath = os.getcwd(myfile)
        print(filepath)