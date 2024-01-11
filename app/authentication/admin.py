from django.contrib import admin
from .models import Cities, Semesters, Desposites, CustomUser, Profile

class CitiesAdmin(admin.ModelAdmin):
    list_display = ['city', 'city_person']
    search_fields = ['city', 'city_person']

class SemestersAdmin(admin.ModelAdmin):
    list_display = ['semester', 'semester_person']
    search_fields = ['semester', 'semester_person']

class DespositesAdmin(admin.ModelAdmin):
    list_display = ['user', 'copy', 'issue_date', 'due_date']
    search_fields = ['user__username', 'copy__book__title', 'issue_date', 'due_date']

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'father_name', 'contact_no', 'identification_no', 'registration_no', 'page_no', 'original_address', 'current_address', 'signature']
    search_fields = ['user__username', 'first_name', 'last_name', 'father_name']

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'faculty', 'semester', 'city', 'gender']
    search_fields = ['username', 'email', 'faculty__faculty_name', 'semester__semester', 'city__city']

admin.site.register(Cities, CitiesAdmin)
admin.site.register(Semesters, SemestersAdmin)
admin.site.register(Desposites, DespositesAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(CustomUser, CustomUserAdmin)