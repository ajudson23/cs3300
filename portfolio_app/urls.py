from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),
path('students/', views.StudentListView.as_view(), name= 'students'),
path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
path('portfolio/', views.portfolioListView.as_view(), name= 'portfolio'),
path('portfolio/<int:pk>', views.portfolioDetailView.as_view(), name='portfolio-detail'),
path('projects/', views.projectListView.as_view(), name= 'project'),
path('project/<int:pk>', views.projectDetailView.as_view(), name='project-detail'),
path('portfolio/<int:portfolio_id>/create_project/', views.createProject, name='create_project'),
path('project/<int:pk>/delete/', views.deleteProject, name='delete-project'),
path('project/<int:pk>/update/', views.updateProject, name='update-project'),
]