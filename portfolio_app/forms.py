
from django.forms import ModelForm
from .models import *

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields=['title', 'description']

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'contact_email', 'is_active', 'about']