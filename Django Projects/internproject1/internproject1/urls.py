"""internproject1 URL Configuration

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
from django.urls import path,re_path,include
from application import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.index_view),
    path('accounts/',include('django.contrib.auth.urls')),
    path('adm/',views.admin_view),
    path('signup/',views.signup_view),
    path('login/',views.login_view),
    path('admin_signup/',views.admin_signup_view),
    path('student_signup/',views.student_signup_view),
    path('employee_signup/',views.employee_signup_view),
    path('admin_login/',views.admin_login_view),
    path('student_login/',views.student_login_view),
    path('employee_login/',views.employee_login_view),
    path('student_table/',views.student_table_view),
    path('employee_table/',views.employee_table_view),
    path('student/',views.student_view),
    path('employee/',views.employee_view),
    path('logout/',views.logout_view),
]
