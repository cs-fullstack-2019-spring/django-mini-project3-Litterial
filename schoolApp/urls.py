from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('submit',views.submit,name='submit'),
    path('enterTeacher',views.enterTeacher,name='enter'),
    path('teacherinfo/<int:ID>/',views.teacherinfo,name='teacherinfo'),
    path('allhours/<int:ID>/',views.allhours,name='allhours'),
    path('deleteCard/<int:ID>/',views.deleteCard,name='deleteCard'),
    path('editCard/<int:ID>/',views.editCard,name='editCard'),



]
