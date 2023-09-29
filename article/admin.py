from django.contrib import admin

# Register your models here.
from .models import Article,Comment

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display=['title','author']
    list_display_links=['title','author']
    search_fields=['title']
    list_filter=['created_data','title']
    class Meta: #bağlamak için meta yazmak önemli
        model = Article #bu class'la 'ArticleAdmini'i Article bağlamış olduk

