from django.contrib import admin
from .models import CourseDetail
from django.utils.html import format_html

# Register your models here.
class CourseDetailAdmin(admin.ModelAdmin):
    def thumbmail(self, object):
        return format_html('<img src="{}" width="40px" style="border-radius:50%" />'.format(object.image.url))
    list_display = ('id', 'thumbmail','description',)
    list_display_links = ('id', 'thumbmail')

admin.site.register(CourseDetail, CourseDetailAdmin)
