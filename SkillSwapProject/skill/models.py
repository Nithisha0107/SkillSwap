from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User
from django.conf import settings

class SkillCategory(BaseModel):
    name = models.CharField(max_length = 250)
    def __str__(self):
        return self.name

class Skill(BaseModel):
    name = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(SkillCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class SkillRequest(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    description = models.TextField(blank = True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending')
    proficiency_level = models.CharField(max_length=30,choices=[('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')])

class SkillOffer(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    availability_from = models.TimeField()
    availability_to = models.TimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending')
    proficiency_level = models.CharField(max_length=30,choices=[('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')])



