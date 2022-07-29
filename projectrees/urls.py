from django.urls import path
from projectrees.views import (
  GetUserProjectreeById, ProjectreeView, ProjectItemView, UpdateProjectree,
  GetUserProjectree, DeleteUserProjectreeById, PublishProjects, ViewPublish,
  UpdateProject, DeleteProject
  )

urlpatterns = [
  path('projectree', ProjectreeView.as_view(), name='projectree'),
  path('project', ProjectItemView.as_view(), name='project'),
  path('update-projectree/<int:projectree_id>/', UpdateProjectree.as_view(), name='update-projectree'),
  path('get-user-projectree', GetUserProjectree.as_view(), name='get-user-projectree'),
  path('projectree/<int:projectree_id>', GetUserProjectreeById.as_view(), name='projectree-detail'),
  path('delete-projectree/<int:projectree_id>', DeleteUserProjectreeById.as_view(), name='delete-projectree'),
  path('publish-projectree/<int:projectree_id>', PublishProjects.as_view(), name='publish-projectree'),
  path('view-publish/<str:publish_name>', ViewPublish.as_view(), name='view-publish-projectree'),
  path('update-project/<int:project_id>/', UpdateProject.as_view(), name='update-project'),
  path('delete-project/<int:project_id>/', DeleteProject.as_view(), name='delete-project'),
]