from django.contrib import admin

# Register your models here.
from blog.models import Author, Publisher, Book


class AutAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


class PubAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')


admin.site.register(Author, AutAdmin)
admin.site.register(Publisher, PubAdmin)
admin.site.register(Book, BookAdmin)
