from django.db import models

# Create your models here.

class Response_types(models.Model):
  name = models.CharField(max_length=255, primary_key=True)
  allowed = models.BooleanField(default=False)
  def __str__(self):
    return self.name
    
class Scope(models.Model):
  name = models.CharField(max_length=255, primary_key=True)
  description = models.TextField(null=True)
  allowed = models.BooleanField(default=False)
  
  def __str__(self):
    return self.name

class Grant_types(models.Model):
  name = models.CharField(max_length=255, primary_key=True)
  allowed = models.BooleanField(default=False)
  def __str__(self):
    return self.name

class Client(models.Model):
  client_secret = models.CharField(max_length=64)
  browser_redirect = models.BooleanField(default=True)
  provider_name = models.CharField(max_length=255)
  client_id = models.CharField(max_length=64)
  redirect_uri = models.CharField(max_length=255)
  implicit_consent = models.BooleanField(default=False)
  response_types = models.ManyToManyField(Response_types)
  grant_types = models.ManyToManyField(Grant_types)
  scope = models.ManyToManyField(Scope) 
  
  def __srt__(self):
    return self.provider_name
  
  class Meta:
    verbose_name_plural = "Clients"
    ordering = ["provider_name"]