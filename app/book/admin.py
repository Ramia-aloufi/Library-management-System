from django.contrib import admin
from .models import Author, Publisher, Faculty, Libraries, Language, Category, Section, Book, EBook, Copy

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    search_fields = ['name', 'location']

class FacultyAdmin(admin.ModelAdmin):
    list_display = ['faculty_name', 'person']
    search_fields = ['faculty_name', 'person']

class LibrariesAdmin(admin.ModelAdmin):
    list_display = ['faculty', 'services', 'email']
    search_fields = ['faculty__faculty_name', 'services', 'email']

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_persian']
    search_fields = ['name', 'category_persian']

class SectionAdmin(admin.ModelAdmin):
    list_display = ['category', 'section', 'section_persian']
    search_fields = ['category__name', 'section', 'section_persian']

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'authors_list', 'publisher', 'section', 'faculty', 'language', 'isbn', 'pages', 'edition', 'publication_year']
    search_fields = ['title', 'authors__first_name', 'authors__last_name', 'publisher__name', 'section__section', 'faculty__faculty_name', 'isbn']

    def authors_list(self, obj):
        return ', '.join([author.__str__() for author in obj.authors.all()])

class EBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'extension']
    search_fields = ['book__title', 'extension']

class CopyAdmin(admin.ModelAdmin):
    list_display = ['book', 'status']
    search_fields = ['book__title', 'status']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Libraries, LibrariesAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(EBook, EBookAdmin)
admin.site.register(Copy, CopyAdmin)
