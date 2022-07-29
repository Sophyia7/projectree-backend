from django.db import models
from accounts.models import User


class ProjectItem(models.Model):
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False, null=True)
  name = models.CharField(max_length=255, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  image = models.URLField(max_length=255, blank=True, null=True)
  programming_language = models.CharField(max_length=255, blank=True, null=True)
  source_code = models.URLField(max_length=255, blank=True, null=True)
  demo_link = models.URLField(max_length=255, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name


  class Meta:
    verbose_name_plural = 'projects'
    db_table = 'projects'
    indexes = [
      models.Index(fields=['name', 'created_at'])
    ]


class Projectree(models.Model):
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False, null=True)
  projectree_name = models.CharField(max_length=255, blank=True)
  title = models.CharField(max_length=100, null=True, blank=True)
  favicon = models.URLField(blank=True, null=True)
  theme = models.CharField(max_length=255, blank=True, null=True)
  project_items = models.ManyToManyField(ProjectItem, blank=True, related_name="projects")
  created_at = models.DateTimeField(auto_now_add=True, null=True)
  updated_at = models.DateTimeField(auto_now=True, null=True)

  def __str__(self):
    return self.projectree_name

  class Meta:
    verbose_name_plural = 'projectrees'
    db_table = 'projectree'
    indexes = [
      models.Index(fields=['user', 'created_at'])
    ]


class PublishedProjects(models.Model):
  name = models.CharField(max_length=255, blank=True)
  projectree = models.ForeignKey(Projectree, on_delete=models.DO_NOTHING, db_constraint=False, null=True)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_constraint=False, null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name_plural = 'published projects'
    db_table = 'published_projects'
    indexes = [
      models.Index(fields=['name', 'projectree', 'user', 'created_at'])
    ] 
