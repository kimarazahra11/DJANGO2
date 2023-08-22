from django.contrib import admin
from .models import Services



class adminservices(admin.ModelAdmin):
    list_display = ['title','content','status']
    list_editable = ["status"]
    search_fields = ['title']
   
admin.site.register(Services,adminservices)   


