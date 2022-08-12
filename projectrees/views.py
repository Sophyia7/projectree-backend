from tokenize import Token
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from projectrees.serializers import (
  ProjectSerializer, ProjectreeSerailizer, PublishedSerializer,
  ViewPublishSerializer
  )
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from rest_framework import status
from projectrees.models import ProjectItem, Projectree, PublishedProjects
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

# This API is used to create a new projectree

class ProjectreeView(GenericAPIView):
  serializer_class = ProjectreeSerailizer
  permission_classes = [IsAuthenticated]

  def post(self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid(): 
      serializer.save(user=request.user)
      return Response(
        {
          "success": True,
          "detail": "Projectree saved successfully",
          "data": serializer.data
        },
        status=status.HTTP_200_OK
      )
    else:
      return Response(
        {
          "success": False,
          "detail": "Error occured",
          "data": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
      )

# This API is used to create a project item

class ProjectItemView(GenericAPIView):
  serializer_class = ProjectSerializer
  permission_classes = [IsAuthenticated]

  def post(self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      serializer.save(user=request.user)

      return Response(
        {
          "success": True,
          "detail": "Project saved successfully",
          "data": serializer.data
        },
        status=status.HTTP_200_OK
      )
    else: 
      return Response(
        {
          "success": False,
          "detail": "Project not saved successfully",
          "data": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
      )


# This API is used to update a projectree by ID

class UpdateProjectree(GenericAPIView):
  serializer_class = ProjectreeSerailizer
  permission_classes = [IsAuthenticated]

  def put(self, request, projectree_id):
    try:
      user = get_object_or_404(User, pk=request.user.id)
      projectree = get_object_or_404(Projectree, pk=projectree_id)
      if user.id == projectree.user.id:
        serializer = self.serializer_class(projectree, data=request.data)

        if serializer.is_valid():
          project_items = request.data.get("project_items")

          for project_item in project_items:
            if ProjectItem.objects.filter(id=project_item).exists():
              project_item = ProjectItem.objects.get(id=project_item)
              projectree.project_items.add(project_item)
            else:
              return Response(
                {
                  "success": False,
                  "detail": "Project item doesn't exist"
                },
                status=status.HTTP_400_BAD_REQUEST
              )

          serializer.save()
          return Response(
            {
              "success": True,
              "detail": "Projectree updated successfully",
              "data": serializer.data
            },
            status=status.HTTP_200_OK
          )
        else:
          return Response(
            {
              "success": False,
              "detail": "Projectree not updated successfully",
              "data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
          )
      else:
        return Response(
          {
            "success": False,
            "detail": "You are not authorized to update this projectree"
          },
          status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
      print(e)
      return Response(
        {
          "success": False,
          "detail": str(e)
        },
        status=status.HTTP_404_NOT_FOUND
      )

# This API is used to update a project by ID

class UpdateProject(GenericAPIView):
  serializer_class = ProjectSerializer
  permission_classes = [IsAuthenticated]

  def put(self, request, project_id):
    try:
      user = get_object_or_404(User, pk=request.user.id)
      project = get_object_or_404(ProjectItem, pk=project_id)

      if user.id == project.user.id:
        serializer = self.serializer_class(project, data=request.data)

        if serializer.is_valid():
          serializer.save()
          return Response(
            {
              "success": True,
              "detail": "Project updated successfully",
              "data": serializer.data
            },
            status=status.HTTP_200_OK
          )
        else:
          return Response(
            {
              "success": False,
              "detail": "Project not updated successfully",
              "data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
          )
      else:
        return Response(
          {
            "success": False,
            "detail": "You are not authorized to update this project"
          },
          status=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
      print(e)
      return Response(
        {
          "success": False,
          "detail": str(e)
        },
        status=status.HTTP_404_NOT_FOUND
      )



# This API is used to get a user projectree
      

class GetUserProjectree(GenericAPIView):
  serializer_class = ProjectreeSerailizer
  permission_classes = [IsAuthenticated]

  def get(self, request):
    user = get_object_or_404(User, pk=request.user.id)
    projectree = Projectree.objects.filter(user=user)
    serializer = self.serializer_class(instance=projectree, many=True)

    return Response(
      {
        "success": True,
        "detail": "Projectree retrieved successfully",
        "data": serializer.data
      },
      status=status.HTTP_200_OK
    )
  
# This API is used to get a user projectree by ID

  
class GetUserProjectreeById(GenericAPIView):
  serializer_class = ProjectreeSerailizer
  permission_classes = [IsAuthenticated]

  def get(self, request, projectree_id):
    user = get_object_or_404(User, pk=request.user.id)
    projectree = Projectree.objects.filter(user=user, id=projectree_id)
    serializer = self.serializer_class(instance=projectree, many=True)

    if Projectree.objects.filter(user=user, id=projectree_id).count() > 0:
      return Response(
        {
          "success": True,
          "detail": "Projectree retrieved successfully",
          "data": serializer.data
        },
        status=status.HTTP_200_OK
      )
    else:
      return Response(
        {
          "success": False,
          "detail": "Projectree does not exist"
        },
        status=status.HTTP_400_BAD_REQUEST
      )


# This API is used to delete a user projectree by ID

class DeleteUserProjectreeById(GenericAPIView):
  serializer_class = ProjectreeSerailizer
  permission_classes = [IsAuthenticated]

  def delete(self, request, projectree_id):
    user = get_object_or_404(User, pk=request.user.id)
    projectree = Projectree.objects.filter(user=user, id=projectree_id)

    if projectree.exists():
      projects = ProjectItem.objects.filter(user=user, projects=projectree_id)

      # delete them in loop
      for project in projects: 
        if ProjectItem.objects.filter(id=project.id).exists():
          project.delete()
        
      # If projectree is published delete it
      if PublishedProjects.objects.filter(projectree=projectree_id).exists():
        published_project = PublishedProjects.objects.get(projectree=projectree_id)
        published_project.delete()

      projectree.delete()

      return Response(
        {
          "success": True,
          "detail": "Projectree deleted successfully"
        },
        status=status.HTTP_200_OK
      )
    else:
      return Response(
        {
          "success": False,
          "detail": "Projectree does not exist"
        },
        status=status.HTTP_400_BAD_REQUEST
      )





#  This API is used to publish a projectree by ID

class PublishProjects(GenericAPIView):
  serializer_class = PublishedSerializer
  permission_classes = [IsAuthenticated]

  def post(self, request, projectree_id):
    user = get_object_or_404(User, pk=request.user.id)
    projectree = Projectree.objects.filter(user=user, id=projectree_id).first()
    serializer = self.serializer_class(data=request.data)
    print(projectree)

    if serializer.is_valid():
      if Projectree.objects.filter(id=projectree_id).exists():
        name = serializer.validated_data.get("name")
        if PublishedProjects.objects.filter(name=name).exists():
          return Response(
            {
              "success": False,
              "detail": "A projectree already exists with this name"
            },
            status=status.HTTP_400_BAD_REQUEST
          )
        if PublishedProjects.objects.filter(projectree=projectree).exists():
          return Response(
            {
              "success": False,
              "detail": "This projectree has already been published"
            },
            status=status.HTTP_400_BAD_REQUEST
          )
        serializer.save(user=request.user, projectree=projectree)
        return Response(
          {
            "success": True,
            "detail": "Projectree published successfully",
            "data": serializer.data
          },
          status=status.HTTP_200_OK
        )
      else:
        return Response(
          {
            "success": False,
            "detail": "Projectree does not exist"
          },
          status=status.HTTP_400_BAD_REQUEST
        )
    else:
      return Response(
        {
          "success": False,
          "detail": "Projectree not published successfully",
          "data": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
      )


# This API is used to view an published projectree by ID

class ViewPublish(GenericAPIView):
  serializer_class = ViewPublishSerializer

  def get(self, request, publish_name):
    if PublishedProjects.objects.filter(name=publish_name).exists():
      publish = PublishedProjects.objects.filter(name=publish_name).first()
      serializer = self.serializer_class(instance=publish)
      return Response(
        {
          "success": True,
          "detail": "Published projectree retrieved successfully",
          "data": serializer.data
        },
        status=status.HTTP_200_OK
      )
    else:
      return Response(
        {
          "success": False,
          "detail": "Published projectree does not exist"
        },
        status=status.HTTP_400_BAD_REQUEST
      )

# This API is used to delete a project by ID

class DeleteProject(GenericAPIView):
  serializer_class = ProjectSerializer
  permission_classes = [IsAuthenticated]

  def delete(self, request, project_id):
    user = get_object_or_404(User, pk=request.user.id)
    project = ProjectItem.objects.filter(user=user, id=project_id).first()

    if ProjectItem.objects.filter(id=project_id).exists():
      project.delete()
      return Response(
        {
          "success": True,
          "detail": "Project deleted successfully"
        },
        status=status.HTTP_200_OK
      )
    else:
      return Response(
        {
          "success": False,
          "detail": "Project does not exist"
        },
        status=status.HTTP_400_BAD_REQUEST
      )



