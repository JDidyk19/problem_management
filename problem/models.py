from django.db import models
from problem_management import settings
from django.utils.text import slugify
from time import time

# generate a slug of name and time
def generate_slug(name):
    new_slug = slugify(name, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Problem(models.Model):
    ''' Problem model '''
    # CHOICES
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
    # DATABASE FIELDS
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='problems', on_delete=models.CASCADE)
    name_problem = models.CharField('Problem name', max_length=150)
    slug = models.SlugField('Url', max_length=150, blank=True, unique=True)
    url_problem = models.CharField('Problem\'s url from some site', max_length=150)
    difficulty = models.CharField('Difficulty', max_length=150, choices=DIFFICULTY, default=NA)
    published = models.DateTimeField('Published date', auto_now_add=True)

    class Meta:
        ordering = ['published']
        verbose_name = "Problem"
        verbose_name_plural = "Problems"

    # TO STRING METHOD
    def __str__(self):
        return self.name_problem

    # SAVE METHOD
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.name_problem)
        super().save(*args, **kwargs)


class Solution(models.Model):
    ''' Solution model '''
    # CHOICES
    accepted = 'Accepted'
    wrong = 'Wrong Answer'
    NA = 'NA'
    STATUS = [
        (accepted, 'Accepted'),
        (wrong, 'Wrong Answer'),
        (NA, 'NA')
    ]

    # DATABASE FIELDS
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    time_submished = models.TextField('Time submished', max_length=300)
    status = models.CharField('Status', max_length=50, choices=STATUS, default=NA)
    runtime = models.CharField('Runtime', max_length=20)
    memory = models.CharField('Memory', max_length=20)
    published = models.DateTimeField('Published date', auto_now_add=True)

    class Meta:
        ordering = ['published']
        verbose_name = "Solution"
        verbose_name_plural = "Solutions"

    # TO STRING METHOD
    def __str__(self):
        return self.problem.name_problem


class Notate(models.Model):
    ''' Notate model '''
    # DATABASE FIELDS
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    notate = models.TextField()
    published = models.DateTimeField('Published date', auto_now_add=True)

    class Meta:
        ordering = ['published']
        verbose_name = "Notate"
        verbose_name_plural = "Notates"

    # TO STRING METHOD
    def __str__(self):
        return self.problem.name_problem
