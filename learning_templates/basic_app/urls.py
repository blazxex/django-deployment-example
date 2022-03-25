from django.urls import path,re_path
from basic_app import views

#template Tagging
app_name = 'basic_app'   #match after url in relative

urlpatterns = [
    re_path(r'^relative/$',views.relative,name='relative'),
    re_path(r'^other/$',views.other,name = 'other'),
]
