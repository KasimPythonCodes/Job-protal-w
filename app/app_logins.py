from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login ,  logout ,authenticate 
from django.contrib import messages
from django.shortcuts import render , HttpResponse ,redirect



class Email_With_Login_User(ModelBackend):
    def authenticate(self , username=None , password=None , **kwargs):
        CustomUser = get_user_model()
        try:
            user= CustomUser.objects.get(email = username)
        except CustomUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


def user_auth_login(request):
    print("KKKKKKKKKKKKKKKKKK")
    return render(request, 'accounts/mylogin.html') 
    
def User_login(request):
    if request.method == 'POST':
        print("HHHHHHHHHHHHHHHHHHH")
        user = Email_With_Login_User.authenticate(request, username=request.POST.get('email') , password=request.POST.get('password'),)
        if user != None:
            login(request , user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('/')
            else:
                messages.error(request , "Email or Password are Invalid !")
                return redirect('login')
        else:
            messages.error(request, "Email or Password are Invalid!!")
            return redirect('login') 
    else:
        return redirect('login')      
    # return render(request , 'accounts/mylogin.html')    
    
def logou_user(request):
    logout(request)
    return redirect('login')    