from django.urls import path
from .views import TaskList,TaskDetails,TaskCreate

urlpatterns = [
    path('',TaskList.as_view() ,name='tasks'),
    path('taskdetail/<int:pk>/',TaskDetails.as_view(),name='taskdetail'),
    path('task-create/',TaskCreate.as_view(),name='task-create')

]
