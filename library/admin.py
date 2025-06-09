from django.contrib import admin
from .models import Author, Book, Records

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Records)


# admin creds:
# username:admin
# pass:admin123