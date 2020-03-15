from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^home/(?P<un>\S+)/$',views.home_view),
    path('apply_for_leave/',views.apply_for_leave_view),
    re_path(r'^approval/(?P<un>\S+)/(?P<days>\d+)/(?P<dt>[0-9]{2}-[0-9]{2}-[0-9]{4}\s+[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{6})/$',views.approval_view),
    path('approval_test/',views.approval_test_view),
    path('pending/',views.pending_view),
    path('cancel/',views.cancel_view),
    path('update/',views.update_view),
    re_path(r'confirm_update/(?P<un>\S+)/$',views.confirm_update_view),
    path('confirm_update_test/',views.confirm_update_test_view),
    path('applied/',views.applied_view),
    path('check_session/',views.check_session_view),
]
