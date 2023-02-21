from django.urls import path,include
from  . import views
app_name='apps'

urlpatterns=[
    path('',views.index,name='home'),
    path('page/',views.home,name='page'),
    path('forms/',views.forms,name='forms'),

]