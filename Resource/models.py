from django.db import models

class Resource(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pdf=models.FileField(upload_to="Resource/pdf/")
    def __str__(self):
        return self.title
        