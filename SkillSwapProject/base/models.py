from django.db import models
from django.conf import settings
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.CharField(max_length=50,null=True,blank=True)
    updated_by = models.CharField(max_length=50,null=True,blank=True)

    class Meta:
        abstract = True
