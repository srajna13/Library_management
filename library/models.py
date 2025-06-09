from django.db import models

# django's user model
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title=models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} (ID: {self.id})"

class Records(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  
    borrow_date = models.DateField(auto_now_add=True)  
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False)   

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"