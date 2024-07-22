from django.contrib import admin
from siteweb.models import Project
from siteweb.models import Contact, Education, Experience, Skill, Resume

# Register your models here.

class AdminProject(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'progress', 'type', 'link', 'description' )

class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'email', 'object', 'message', 'submitted_at' )

class AdminEducation(admin.ModelAdmin):
    list_display = ('resume', 'institution', 'degree', 'start_date', 'end_date', 'description' )

class AdminExperience(admin.ModelAdmin):
    list_display = ('resume', 'job_title', 'company', 'start_date', 'end_date', 'description' )

class AdminSkill(admin.ModelAdmin):
    list_display = ('resume', 'name', 'level')

class Adminresume(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'summary')


admin.site.register(Project, AdminProject)
admin.site.register(Contact,AdminContact)
admin.site.register(Education, AdminEducation)
admin.site.register(Experience, AdminExperience)
admin.site.register(Skill, AdminSkill)
admin.site.register(Resume, Adminresume)
