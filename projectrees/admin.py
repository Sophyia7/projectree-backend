from django.contrib import admin
from projectrees.models import Projectree, ProjectItem, PublishedProjects

# Register your models here.
admin.site.register(Projectree)
admin.site.register(ProjectItem)
admin.site.register(PublishedProjects)