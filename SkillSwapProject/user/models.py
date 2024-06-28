from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from base.models import BaseModel
from skill.models import SkillRequest,SkillOffer

class User(AbstractUser,BaseModel):
    first_name = models.CharField(max_length=100,unique =True)
    last_name = models.CharField(max_length=100,unique =True)
    phone_number = PhoneNumberField()
    qualification = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    occupation = models.CharField(max_length=250, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    gender = models.CharField(max_length=10,blank=True)
    skill_request = models.ManyToManyField('skill.Skill',through=SkillRequest,related_name='requested_by')
    skill_offer = models.ManyToManyField('skill.Skill',through=SkillOffer,related_name='offered_by')


class Data(BaseModel):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    class Meta:
        indexes = [
            models.Index(fields=['name', 'age']),
            models.Index(fields=['id'])
        ]


