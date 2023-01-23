from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from app.models import *
admin.site.register(CustomUser)
admin.site.register(Resume)
admin.site.register(job_post)
admin.site.unregister(Group)

# admin.site.register(ProfileAvatar)
# admin.site.register(ProfileAvatarFile)







