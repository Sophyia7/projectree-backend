from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from projectrees.serializers import (
  ProjectSerializer, ProjectreeSerailizer, PublishedSerializer
  )
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from rest_framework import status
from projectrees.models import ProjectItem, Projectree, PublishedProjects


# This API is used to create a new projectree

class ProjectreeView(GenericAPIView):
  serializer_class = ProjectreeSerailizer
  permission_classes = [IsAuthenticated]

  def post(self, request):
    serializer = self.serializer_class(data=request.data)

    if serializer.is_valid():
      name = serializer.validated_data.get("projectree_name")
      if Projectree.objects.filter(projectree_name=name).exists():
        return Response(
          {
            "message": str(name) + " is already in use. Choose another name for your projectree"
          },
          status=status.HTTP_400_BAD_REQUEST
        )
      else: 
        serializer.save()
        return Response(
          {
            "message": "Projectree saved successfully",
            "data": serializer.data
          },
          status=status.HTTP_200_OK
        )
    else:
      return Response(
        {
          "message": "Error occured",
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
      serializer.save()

      return Response(
        {
          "message": "Project saved successfully",
          "data": serializer.data
        },
        status=status.HTTP_200_OK
      )
    else: 
      return Response(
        {
          "message": "Project not saved successfully",
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
                  "error": "Project item doesn't exist"
                },
                status=status.HTTP_400_BAD_REQUEST
              )
    
    

          serializer.save()
          return Response(
            {
              "message": "Projectree updated successfully",
              "data": serializer.data
            },
            status=status.HTTP_200_OK
          )
        else:
          return Response(
            {
              "message": "Projectree not updated successfully",
              "data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
          )
    except Exception as e:
      print(e)
      return Response(
        {
          "message": str(e)
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
              "message": "Project updated successfully",
              "data": serializer.data
            },
            status=status.HTTP_200_OK
          )
        else:
          return Response(
            {
              "message": "Project not updated successfully",
              "data": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
          )
    except Exception as e:
      print(e)
      return Response(
        {
          "message": str(e)
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
        "message": "Projectree retrieved successfully",
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
          "message": "Projectree retrieved successfully",
          "data": serializer.data
        },
        status=status.HTTP_200_OK
      )
    else:
      return Response(
        {
          "message": "Projectree does not exist"
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
      projectree.delete()
      return Response(
        {
          "message": "Projectree deleted successfully"
        },
        status=status.HTTP_200_OK
      )
    else:
      return Response(
        {
          "message": "Projectree does not exist"
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
        serializer.save()
        return Response(
          {
            "message": "Projectree published successfully",
            "data": serializer.data
          },
          status=status.HTTP_200_OK
        )
      else:
        return Response(
          {
            "message": "Projectree does not exist"
          },
          status=status.HTTP_400_BAD_REQUEST
        )
    else:
      return Response(
        {
          "message": "Projectree not published successfully",
          "data": serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
      )


# This API is used to view an published projectree by ID

class ViewPublish(GenericAPIView):
  serializer_class = PublishedSerializer
  permission_classes = [IsAuthenticated]

  def get(self, request, publish_name):
    user = get_object_or_404(User, pk=request.user.id)
    publish = PublishedProjects.objects.filter(user=user, name=publish_name).first()
    serializer = self.serializer_class(instance=publish)

    if PublishedProjects.objects.filter(user=user, name=publish_name).exists():
      return Response(
        {
          "message": "Projectree retrieved successfully",
          "data": serializer.data
        },
        status=status.HTTP_200_OK
      )
    else:
      return Response(
        {
          "message": "Projectree does not exist"
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
          "message": "Project deleted successfully"
        },
        status=status.HTTP_200_OK
      )
    else:
      return Response(
        {
          "message": "Project does not exist"
        },
        status=status.HTTP_400_BAD_REQUEST
      )



