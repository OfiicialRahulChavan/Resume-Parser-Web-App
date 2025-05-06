from django.db import models

class ResumeUpload(models.Model):
    file = models.FileField(upload_to='resumes/')