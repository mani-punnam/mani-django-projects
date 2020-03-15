from django.urls import path,re_path
from . import views
urlpatterns=[
    path('login/',views.login_view),
    path('logout/',views.logout_view),
    path('change_password/',views.change_password_view),
    path('change_password_test/',views.change_password_test_view),
    re_path(r'^confirm_password/(?P<un>\S+)/$',views.confirm_password_view),
    path('confirm_password_test/',views.confirm_password_test_view),
    
]
