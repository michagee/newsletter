from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Archiv(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)

class Newsletter(models.Model):
    issue = models.AutoField()
    header = models.OneToOneField(Header, on_delete=models.CASCADE)
    content = models.OneToOneField(TextContent, on_delete=models.CASCADE)


class Header(models.Model):
    DOCTYPE = (
        ("html5", "<!DOCTYPE html>"),
        ("XHTML", "<!DOCTYPE html>"),
    )
    title = models.CharField(max_length=100)
    date = models.DateField()


class TextContent(models.Model):
    heading = models.CharField()
    subheading = models.CharField(blank=True)
    #picture = models.FileField()



class Section(models.Model):
    title = models.CharField(max_length=200)
