from django.contrib import admin

# Register your models here.
from .models import Book,author,review

class ProductAdmin(admin.ModelAdmin):
    list_display=['title']
    
    


admin.site.register(Book,ProductAdmin)    
admin.site.register(author)    
admin.site.register(review)    