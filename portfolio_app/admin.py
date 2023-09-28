from django.contrib import admin
from .models import *


# Register your models here so they can be edited in admin panel
admin.site.register(Student)
admin.site.register(Project)
admin.site.register(Portfolio)
admin.site.register(ProjectsInPortfolio)