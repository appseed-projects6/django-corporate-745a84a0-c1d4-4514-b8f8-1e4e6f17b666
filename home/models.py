# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Partners(models.Model):

    #__Partners_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    officialname = models.CharField(max_length=255, null=True, blank=True)

    #__Partners_FIELDS__END

    class Meta:
        verbose_name        = _("Partners")
        verbose_name_plural = _("Partners")


class Creators(models.Model):

    #__Creators_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    officialname = models.CharField(max_length=255, null=True, blank=True)

    #__Creators_FIELDS__END

    class Meta:
        verbose_name        = _("Creators")
        verbose_name_plural = _("Creators")


class Services(models.Model):

    #__Services_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Services_FIELDS__END

    class Meta:
        verbose_name        = _("Services")
        verbose_name_plural = _("Services")



#__MODELS__END
