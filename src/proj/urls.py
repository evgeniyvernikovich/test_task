"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from books import views as book_views
from authors import views as author_views
from home_page.views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('b_create/', book_views.CreateBook.as_view()),
    path('b_delete/<int:pk>', book_views.DeleteBook.as_view()),
    path('b_detail/<int:pk>', book_views.ShowBook.as_view()),
    path('b_update/<int:pk>', book_views.UpdateBook.as_view()),
    path('b_show/', book_views.ListBooks.as_view()),
    path('a_create/', author_views.CreateAuthor.as_view()),
    path('a_delete/<int:pk>', author_views.DeleteAuthor.as_view()),
    path('a_detail/<int:pk>', author_views.ShowAuthor.as_view()),
    path('a_update/<int:pk>', author_views.UpdateAuthor.as_view()),
    path('a_show/', author_views.ListAuthors.as_view()),
    path('', HomePage.as_view()),
]
