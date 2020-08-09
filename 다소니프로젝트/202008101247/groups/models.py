from django.db import models
from django.conf import settings
from maps.models import Spot

class Drama(models.Model):
    drama_name = models.CharField(max_length=500)
    drama_img = models.CharField(max_length=500)   
    drama_kind = models.CharField(max_length=500)  

class Actor(models.Model):
    actor_name = models.CharField(max_length=500)
    actor_img = models.CharField(max_length=500)
    drama_cd = models.ForeignKey(Drama, on_delete=models.CASCADE, null=True)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_actor', null=True)

class Show(models.Model):
    show_name = models.CharField(max_length=500)
    show_img = models.CharField(max_length=500)      

class Showman(models.Model):
    showman_name = models.CharField(max_length=500)
    showman_img = models.CharField(max_length=500)
    show_cd = models.ForeignKey(Show, on_delete=models.CASCADE, null=True)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_show', null=True)

class Group(models.Model):
    group_name = models.CharField(max_length=500)
    group_img = models.CharField(max_length=500)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_group', null=True)

class Singer(models.Model):
    singer_name = models.CharField(max_length=500)
    singer_img = models.CharField(max_length=500)
    group_cd = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    spot_cd = models.ManyToManyField(Spot, related_name='spot_singer', null=True)
