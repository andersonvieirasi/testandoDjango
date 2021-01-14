from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', "created_date",
    'published_date', "author", 
    "categories", "approved"
    ]
    search_fields = ['title']
    ordering = ["title"]
    
    #def get_queryset(self,request):
    #	return Post.objects.filter(approved=True)



admin.site.register(Post, PostAdmin)