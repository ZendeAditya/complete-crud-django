from django.urls import path 
from . views import home,add_student,all_student,edit_student,delete_student,search

urlpatterns = [
    path('',home,name='home'),
    path('add_student/',add_student,name="add_student"),
    path('all_student/',all_student,name="all_student"),
    path('edit_student/<str:name>/',edit_student,name="edit_student"),
    path('delete_student/<str:name>/',delete_student,name="delete_student"),
    path('search/',search,name='search')
]
