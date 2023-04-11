from django.db import models

class contactinfo(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=1000)
    info = models.TextField(max_length=1000)

class appointment(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=1000)
    staff = models.CharField(max_length=150)
    date = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    reason = models.TextField(max_length=2000)

class userprofile(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=1000)
    petname = models.CharField(max_length=150)
    lastvisit = models.DateTimeField((""),auto_now=False, auto_now_add=False)
    staff = models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.info