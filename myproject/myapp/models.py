from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    title =  models.CharField(max_length=64,  default="no title yet")
    description = models.CharField(max_length=500, default="no description yet" )
    search_tags = models.ManyToManyField('Tag',blank = True, related_name='posts')

    def get_absolute_url(self):
        print('ERIGAL')
        print("id "+str(self.id))
        id = self.id
        return reverse('cr', kwargs={'id': id})


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'title': self.title})

    def __str__(self):
        return self.title