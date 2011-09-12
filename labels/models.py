from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

class Tag(models.Model):
    name = models.CharField(max_length=100, blank=True)
    slogan1 = models.CharField(max_length=100, blank=True)
    slogan2 = models.CharField(max_length=100, blank=True)
    contact1 = models.CharField(max_length=100, blank=True)
    contact2 = models.CharField(max_length=100, blank=True)
    contact3 = models.CharField(max_length=100, blank=True)
    url = models.URLField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='labels/static/logos', blank=True)
    qrcode = models.ImageField(upload_to='labels/static/qrcodes', blank=True)
    #version = models.ForeignKey('TagVersion', blank=True, null=True)
    author = models.CharField(max_length=100, blank=True)
    template = models.CharField(max_length=100, blank=True)
    entered = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
        
    def __unicode__(self):
        return self.name
    
class TagVersion(models.Model):
    tag = models.ForeignKey(Tag)
    version_num = models.PositiveIntegerField(max_length=100, blank=True)
    entered = entered = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s v%s" %(self.tag.name, self.version_num)
    
@receiver(post_save, sender=Tag)
def tag_save_handler(sender, **kwargs):
    # Check to see if tag already exits
    tag = kwargs['instance']   
    tv = TagVersion.objects.filter(tag=tag)
    if tv:
        # Add a new version
        tv = tv[0]
        version_num = tv.version_num + 1  
    else:
        # Create a new version
        version_num = 1
    tv = TagVersion(version_num=version_num, tag=tag)
    tv.save()