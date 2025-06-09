from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('books/', views.book_list, name='book_list'),
    path('authors/', views.author_list, name='author_list'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:record_id>/', views.return_book, name='return_book'),
    path('my_borrows', views.my_borrows, name='my_borrows'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/library/'), name='logout'),
    path('login/', auth_views.LoginView.as_view(next_page='/library/'), name='login'),
]