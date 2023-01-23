from django.contrib import admin
from django.urls import path, include ,re_path
from django.urls import path, include , re_path 

from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url , patterns
# from django.conf.urls




# urlpatterns = patterns('',
# url(r'^ckeditor/', include('ckeditor.urls')),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include("app.urls")),
    # re_path(r'^ckeditor/', include('ckeditor.urls')),
    # re_path(r'^ckeditor/', include('ckeditor.urls')),
 ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
