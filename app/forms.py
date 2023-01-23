from django import forms
from app.models import *

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('image',)

#     def clean_image(self):
#         image = self.cleaned_data.get('image', False)
#         if not self.instance.image == image:
#             # validate image
#         return None
class POST_VIEWS_FORM(forms.ModelForm):
    
    class Meta:
        model=job_post
        fields =('job_profile','company_name',
                 'job_location','min_salary',
                 'max_salary','package',
                 'Vacancy','job_description')
        labels ={'job_profile':'Job Profile'}
        error_messages ={'job_profile':{'required':'The Job Profile is required'},
                         'company_name':{'required':'The Company Name is required'},
                         'job_location':{'required':'The Job Location is required'},
                         'min_salary':{'required':'The Min Salary is required '},
                         'max_salary':{'required':'The Max Salary is required'},
                         'package':{'required':'The Package is required'},
                         'Vacancy':{'required':'The Vacancy is required'},
                         'job_description':{'required':'The Job Description is required'},

                         
                         }
        
        widgets = {
            'job_profile':forms.TextInput(attrs={'class':'form-control'}),
            'company_name':forms.TextInput(attrs={'class':'form-control'}),
            'job_location':forms.TextInput(attrs={'class':'form-control'}),
            'min_salary':forms.NumberInput(attrs={'class':'form-control'} ),
            'max_salary':forms.NumberInput(attrs={'class':'form-control',}),
            'package':forms.TextInput(attrs={'class':'form-control'}),
            'Vacancy':forms.NumberInput(attrs={'class':'form-control',}),
            'job_description':forms.Textarea(attrs={'class':'form-control'}),
            # 'job_skill':forms.Textarea(attrs={'class':'form-control'}),
            # 'job_experience':forms.Textarea(attrs={'class':'form-control'}),
        }
        
    def clean_values(self):
        job_profile=self.cleaned_data.get('job_profile')
        company_name=self.cleaned_data.get('company_name')
        job_location=self.cleaned_data.get('job_location')
        min_salary=self.cleaned_data.get('min_salary')
        max_salary=self.cleaned_data.get('max_salary')
        package=self.cleaned_data.get('package')
        Vacancy=self.cleaned_data.get('Vacancy')
        job_description=self.cleaned_data.get('job_description')
        
        # if len(company_name) <= 4:
        #     raise forms.ValidationError("Enter more than or equal 4 ")
        # return company_name
        # elif len(job_location)<=4:
        #     raise forms.ValidationError("Enter more than or equal 4 ")
        # elif len(min_salary)<2:
        #     raise forms.ValidationError("Enter more than or equal 2")
        # elif len(max_salary)<2:
        #     raise forms.ValidationError("Enter more than or equal 2")
        # elif len(package)<2:
        #     raise forms.ValidationError("Enter more than or equal 2")
        
        # elif len(Vacancy)<1:
        #     raise forms.ValidationError("Enter more than or equal 1")
        
        # elif len(job_description)<10:
        #     raise forms.ValidationError("Enter more than or equal 10")
        
         


