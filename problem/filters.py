import django_filters
from .models import Problem


class ProductFilter(django_filters.FilterSet):
    Easy = 'Easy'
    Medium = 'Medium'
    Hard = 'Hard'
    NA = 'NA'
    DIFFICULTY = [
        (NA, 'NA'),
        (Easy, 'Easy'),
        (Medium, 'Medium'),
        (Hard, 'Hard'),
    ]

    #search problem
    name_problem = django_filters.CharFilter(field_name='name_problem', lookup_expr='icontains')
    difficulty = django_filters.ChoiceFilter(field_name='difficulty', empty_label='Difficulty', choices=DIFFICULTY)

    class Meta:
        model = Problem
        fields = ['name_problem', 'difficulty']