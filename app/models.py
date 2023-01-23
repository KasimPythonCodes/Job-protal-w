from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
import uuid
# Create your models here.
from django.core.validators import FileExtensionValidator


# class ProfileAvatar(models.Model):
#     avatar = models.ImageField(upload_to = "image/avatar", validators=[FileExtensionValidator(allowed_extensions=['png','jpg'])])
#     name = models.CharField(max_length=200, null=True)
# class ProfileAvatarFile(models.Model):
#     avatar = models.FileField(upload_to = "File", validators=[FileExtensionValidator(allowed_extensions=['doc','docx','pdf'])])


class CUMMONID(models.Model):
    id = models.UUIDField(primary_key=True ,editable=False , unique=True , default = uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    class Meta:
        abstract =True


class CustomUser(AbstractUser):
    user_choise = (('1','Super-Admin') , ('2',"Company"))
    user_type=models.CharField(default=1,choices=user_choise,max_length=15)
    profile_pic = models.ImageField(upload_to="User/Upload", height_field=None, width_field=None, max_length=None)
    
    
class Resume(CUMMONID):
    job_choice = (
        ('Desinger','Desinger') ,
        ('software engineer',"software engineer"),
        ('Backend Developer',"Backend Developer"),
        ('Forentend Developer',"Forentend Developer"),
        ('UI/UX Desinger',"UI/UX Desinger"),
        
    )
    job_type = (
        (
            ('permanent','permanent'),
            ('Temporary','Temporary'),
            ('Contract','Contract'),

        )
    )
    
    remote_type = (
        (
            ('REMOTE','REMOTE'),
            ('ONSITE','ONSITE'),
            ('HYBRID','HYBRID'),

        )
    )
    
    # admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True,)
    last_name = models.CharField(max_length=20, blank=True,)
    remote_type = models.CharField(choices=remote_type,max_length=20, blank=True,)
    email = models.EmailField(max_length=254)
    job_profile= models.CharField(choices=job_choice ,max_length=250, blank=True,)
    phone_number= models.CharField(max_length=12, blank=True,)
    work_expriance= models.CharField(max_length=5, blank=True,)
    job_type = models.CharField(choices=job_type,max_length=20, blank=True,)
    doc= models.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx'])] , null=True , blank=True)  
    zipcode= models.CharField(max_length=5, blank=True,)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=False, auto_now=True,null=True,blank=True)  
    
    
    def __str__(self):
        return str(self.id)


class job_post(CUMMONID):
    job_profile= models.CharField(max_length=100 ,null=True)
    company_name = models.CharField(max_length=100,null=True)
    job_location = models.CharField(max_length=100,null=True)
    min_salary = models.IntegerField(null=True)
    max_salary = models.IntegerField(null=True)
    Vacancy = models.IntegerField(null=True,)
    date =models.DateField(auto_now_add=True)
    package = models.CharField(max_length=10,null=True)
    
    # date =models.DateField(auto_now_add=False)
    job_description = RichTextField(null=True)
    # job_skill = RichTextField(null=True)
    # job_experience = RichTextField(null=True)

    def __str__(self):
        return str(self.id) +"    " + "   " + (self.job_profile + "  " + "   " + self.job_location)