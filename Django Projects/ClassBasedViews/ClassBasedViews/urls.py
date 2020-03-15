"""ClassBasedViews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from application import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',views.test_view),
    path('a/',views.SampleView.as_view()),
    path('b/',views.SampleTemplateView.as_view()),
    path('info/',views.InfoView.as_view()),
    path('books_list/',views.BooksList.as_view(),name='home'),
    re_path(r'^(?P<pk>\d+)/$',views.BooksDetail.as_view(),name='detail'),
    path('create/',views.BooksCreate.as_view()),
    re_path(r'^update/(?P<pk>\d+)/$',views.BooksUpdate.as_view()),
    re_path(r'^delete/(?P<pk>\d+)/$',views.BooksDelete.as_view()),
]
