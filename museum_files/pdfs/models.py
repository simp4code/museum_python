from django.db import models

# Create your models here.
class ImportFile(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_image = models.ImageField(null=True,blank=True,upload_to='images/', default='images/questionmark.jpeg')
    file_name = models.CharField(max_length=255)
    file_abstract = models.TextField()
    file_pdf = models.FileField(upload_to='pdf_files/')
    
    def __str__(self) -> str:
        return self.file_name

class AdminLogin(models.Model):
    user_name = models.CharField(max_length=255)
    user_pass = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.user_name


