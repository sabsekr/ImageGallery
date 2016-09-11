"""
Create the model. The model is Photo and has two attributes, the image and the hashtag
for the image. Specify to which directory the image should be uploaded.
"""
from __future__ import unicode_literals
from django.db import models


class Photo(models.Model):
    tag_text = models.CharField(max_length=200)
    image_upload = models.ImageField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.tag_text


