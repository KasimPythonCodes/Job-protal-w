from app.models import*
from app.serializers import*
from rest_framework.mixins import*
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet 


class  jobserializerfunction(ModelViewSet):
    queryset = job_post.objects.all() 
    serializer_class = Job_Post_Serializers
    print(serializer_class)


class jobserializerfunctiongeneric(GenericAPIView , ListModelMixin):
    def get_queryset(self):
        jobpost = job_post.objects.all()
        return jobpost
    serializer_class = Job_Post_Serializers
    
    def get(self, request):
        return self.list(request)
        

    