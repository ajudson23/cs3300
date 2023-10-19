from typing import Any
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
#from django.urls import reverse

# Create your views here.
def index(request):
   student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
   print("active portfolio query set", student_active_portfolios)
   return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})

class StudentListView(generic.ListView):
   model = Student
class StudentDetailView(generic.DetailView):
   model = Student

class portfolioListView(generic.ListView):
   model = Portfolio
class portfolioDetailView(generic.DetailView):
   model = Portfolio

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      portfolio = self.get_object()
      context['projects'] = Project.objects.filter(portfolio=portfolio)
      return context

class projectListView(generic.ListView):
   model = Project
class projectDetailView(generic.DetailView):
   model = Project

def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    
    if request.method == 'POST':
        # Create a new dictionary with form data and portfolio_id
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id

        form = ProjectForm(project_data)
        if form.is_valid():
            # Save the form without committing to the database
            project = form.save(commit=False)
            # Set the portfolio relationship
            project.portfolio = portfolio
            project.save()

            # Redirect back to the portfolio detail page
            return redirect('portfolio-detail', portfolio_id)

    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)



def deleteProject(request, pk):
   project = get_object_or_404(Project, pk=pk)
   if request.method == 'POST':
      project.delete()
      return redirect('portfolio-detail', pk=project.portfolio.id)
   return render(request, 'portfolio_app/project_delete.html', {'project': project})

def updateProject(request, pk):
   project = get_object_or_404(Project, pk=pk)
   if request.method == 'POST':
      form = ProjectForm(request.POST, instance=project)
      if form.is_valid():
         form.save()
         return redirect('portfolio-detail', pk=project.portfolio.id)
   else:
      form = ProjectForm(instance=project)
   context = {'form': form, 'project': project}
   return render(request, 'portfolio_app/update_project.html', context)

def updatePortfolio(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('student-detail', pk=portfolio.student.pk)
    else:
        form = PortfolioForm(instance=portfolio)
    context = {'form': form, 'portfolio': portfolio}
    return render(request, 'portfolio_app/update_portfolio.html', context)


