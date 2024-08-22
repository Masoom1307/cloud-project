from django.contrib import admin
from .models import Issue, Module, Course

# Custom admin for the Issue model
class IssueAdmin(admin.ModelAdmin):
    list_display = ('type', 'room', 'urgent', 'date_submitted', 'author')
    list_filter = ('type', 'urgent', 'date_submitted')
    search_fields = ('type', 'room', 'details', 'author__username')
    date_hierarchy = 'date_submitted'
    ordering = ('-date_submitted',)

# Custom admin for the Module model
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'code', 'credit', 'category', 'availability', 'created_at')
    list_filter = ('category', 'availability', 'created_at')
    search_fields = ('title', 'code', 'description')
    filter_horizontal = ('allowed_courses',)
    ordering = ('title',)

# Custom admin for the Course model
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    ordering = ('name',)

# Register your models with custom admin classes
admin.site.register(Issue, IssueAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Course, CourseAdmin)
