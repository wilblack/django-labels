from labels.models import Tag, TagVersion
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "slogan1", "contact1", "url", "author", "entered"]
    
        
class TagVersionAdmin(admin.ModelAdmin):
    list_display = ['tag','version_num', 'entered']
    

admin.site.register(Tag, TagAdmin)
admin.site.register(TagVersion, TagVersionAdmin)
