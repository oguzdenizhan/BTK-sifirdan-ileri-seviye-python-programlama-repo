from django.contrib import admin
from .models import Movie

# http://127.0.0.1:8000/admin

class MovieAdmin(admin.ModelAdmin):
    list_display=("id","name","created_date","isPublished")
    list_display_links= ("id","name")
    list_filter= ("created_date",)
    list_editable=('isPublished',)
    search_fields=("name","description")
    list_per_page = 20
# Register your models here.

admin.site.register(Movie,MovieAdmin)