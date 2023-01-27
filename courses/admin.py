from django.contrib import admin

from .models import Course


# Customização do Admin
class CourseAdmin(admin.ModelAdmin):
    # Campos do relatório
    list_display = ['name', 'slug', 'start_date', 'create_at']
    # Campos para filtro
    search_fields = ['name', 'slug']
    # Preenchimento automático do slug
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
admin.site.register(Course, CourseAdmin)
