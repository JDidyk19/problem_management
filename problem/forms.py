from django import forms
from .models import Problem, Solution, Notate


class ProblemCreateForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = ['name_problem', 'url_problem', 'difficulty']

class AddSolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['time_submished', 'status']


class AddNotateForm(forms.ModelForm):
    class Meta:
        model = Notate
        fields = ['notate']


class EditNotateForm(forms.ModelForm):
    class Meta:
        model = Notate
        fields = ['notate']
