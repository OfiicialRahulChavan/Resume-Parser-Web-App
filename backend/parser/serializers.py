from rest_framework import serializers
from .models import ResumeUpload

class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUpload
        fields = ['file']