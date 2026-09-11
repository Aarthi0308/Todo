from django.urls import path
from . import views
urlpatterns = [
    path('addTask/',views.addtask,name='addtask'),
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('mark_as_undone/<int:id>',views.mark_as_undone,name='mark_as_undone'),

    # edit feature
    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),



]