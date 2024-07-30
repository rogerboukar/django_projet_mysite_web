from django.contrib import admin
from siteweb.models import Project
from siteweb.models import Contact, Education, Experience, Skill, Resume, Language

# Register your models here.

class AdminProject(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'progress', 'type', 'link', 'description' )

class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'email', 'object', 'message', 'submitted_at' )

class AdminEducation(admin.ModelAdmin):
    list_display = ('id', 'institution', 'degree', 'start_date', 'end_date', 'description' )

class AdminExperience(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'company', 'start_date', 'end_date', 'description' )

class AdminSkill(admin.ModelAdmin):
    list_display = ('id', 'name', 'level')

class AdminResume(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address', 'birth_date', 'nationality', 'marital_status', 'summary')


class AdminLanguage(admin.ModelAdmin):
    list_display = ('id', 'language', 'proficiency')


admin.site.register(Project, AdminProject)
admin.site.register(Contact,AdminContact)
admin.site.register(Education, AdminEducation)
admin.site.register(Experience, AdminExperience)
admin.site.register(Skill, AdminSkill)
admin.site.register(Resume, AdminResume)
admin.site.register(Language, AdminLanguage)
