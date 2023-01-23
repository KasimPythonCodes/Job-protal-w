from django.urls import path, include , re_path 
from app.views import*
from app.Resumes_Views_Admin import*
from app.app_logins import*
from app.User_app import*
from django.conf import settings 
from django.conf.urls.static import static

# from django.conf.urls import url/

"""
    Serializer class Routers
"""
from rest_framework.routers import DefaultRouter
from app.Job_Serializer import*
router = DefaultRouter()
router.register('job-post-user'  , jobserializerfunction , basename='job-post-user'),
# router.register('user' , jobserializerfunctiongeneric , basename='user'),
















urlpatterns = [
    # Start Serializer api
    path('api/', include(router.urls)),
    path('user' , jobserializerfunctiongeneric.as_view() , ),
    # End serializer Api
    path('resume/' ,USER_RESUME_POST , name='resume'),
    
    path('resume-delete/<slug:id>',ResumeDelete ,name='resume-delete'),
    path('show-resume/', view_resume , name='show-resume'),
    path('resume-resume-view-delete/<slug:id>',    Resume_Views_Delete ,name='resume-view-delete'),
    path('user-login/',  User_login, name='user-login'),
    path('login/',  user_auth_login, name='login'),
    path('logout/', logou_user, name='logout'),
    path('search/',  SEARCH_BAR_ACTIVATE_RESUME, name='search'),
    path('post-search/', SEARCH_BAR_ACTIVATE_VIEWS_POST, name='post-search'),
    
    path('post-view/',VIEWS_POST, name='post-view'),
    path('addpost/',ADD_POST, name='addpost'),
    path('post-update/<slug:id>/',UPDATE_POST, name='post-update'),
    path('post-delete/<slug:id>/',DELETE_POST, name='post-delete'),
    path('edit-post/<slug:id>/',EDIT_POST_DATA, name='edit-post'),


    

    
    
    
    
    
    
    
    
    
    path('', index , name='home'),
    
    # path('download-pdf/<int:pdfSlug>',Download_all , name='download'),
    # path('download-doc/<int:pdfSlug>',    Download_all_doc , name='download'),
    # re_path(r'^download/$/',Download_all , name='download'),
    # path('pagination' ,    Paginator_all , name='pagination'),
    # re_path(r'^.*\.*', pages, name='pages'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

