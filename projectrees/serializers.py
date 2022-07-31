from unicodedata import name
from projectrees.models import ProjectItem, Projectree, PublishedProjects
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectItem
    fields = (
      'id', 'name', 'description', 'image', 'programming_language', 
      'source_code', 'demo_link', 'created_at'
      )

class ProjectreeSerailizer(serializers.ModelSerializer):
  project_items = ProjectSerializer(read_only=True, many=True)

  class Meta:
    model = Projectree
    fields = (
      'id', 'projectree_name', 'title', 'favicon', 
      'theme', 'project_items', 'created_at', 'updated_at',
    )

 

class PublishedSerializer(serializers.ModelSerializer):
  class Meta:
    model = PublishedProjects
    fields = (
       'name',  
    )

  def create(self, validated_data):
    print("Data: ", validated_data)
    p_project = PublishedProjects.objects.create(name=validated_data['name'], projectree=validated_data['projectree'], user=validated_data['user'])
    p_project.save()
    return validated_data