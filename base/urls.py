from django.urls import path
from .views import *

urlpatterns = [
    path('',TaskList.as_view() ,name='tasks'),
    path('taskdetail/<int:pk>/',TaskDetails.as_view(),name='taskdetail'),
    path('task-create/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>',TaskEdit.as_view(),name='task-update'),
    path('task-delete/<int:pk>',TaskDelete.as_view(),name="task-delete"),
    path('login-app',CustomeLoginView.as_view(),name='login')

]
