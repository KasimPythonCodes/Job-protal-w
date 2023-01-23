from app.models import*
from rest_framework import  serializers

class Job_Post_Serializers(serializers.ModelSerializer):
    class Meta:
        model = job_post
        fields= '__all__'