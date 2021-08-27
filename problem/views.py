from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Problem, Solution, Notate
from .forms import ProblemCreateForm, AddSolutionForm, AddNotateForm


def my_problems(request):
    problems = Problem.objects.filter(user_id=request.user.id).annotate(num_solution=Count('solution')).only(
        'name_problem', 'slug', 'difficulty'
    )

    context = {
        'problems': problems,
    }
    return render(request, 'problem/my_problems.html', context)


def detail_problem(request, slug):
    problem = Problem.objects.get(slug=slug)
    solutions = Solution.objects.filter(problem_id=problem.pk)
    notates = Notate.objects.filter(problem_id=problem.pk)

    context = {
        'problem': problem,
        'solutions': solutions,
        'notates': notates,
    }
    return render(request, 'problem/problem_detail.html', context)


def add_problem(request):
    if request.method == 'POST':
        form = ProblemCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()
            return redirect('detail_problem', slug=problem.slug)
        return redirect('my_problems')
    else:
        form = ProblemCreateForm(request.POST or None, request.FILES or None)

        context = {
            'add_problem': form
        }
    return render(request, 'problem/add_problem_form.html', context)


def add_solution(request, slug):
    if request.method == 'POST':
        problem = Problem.objects.get(slug=slug)
        form = AddSolutionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            solution = form.save(commit=False)
            solution.problem = problem
            solution.save()
            messages.add_message(request, messages.INFO, 'Solution added successfully')
            return redirect('detail_problem', slug=problem.slug)
        return redirect('detail_problem', slug=problem.slug)
    else:
        form = AddSolutionForm(request.POST or None, request.FILES or None)

        context = {
            'add_solution': form,
        }
    return render(request, 'problem/add_solution.html', context)


def add_notate(request, slug):
    if request.method == 'POST':
        problem = Problem.objects.get(slug=slug)
        form = AddNotateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            notate = form.save(commit=False)
            notate.problem = problem
            notate.save()
            return redirect('detail_problem', slug=problem.slug)
        # Написати message
        return redirect('detail_problem', slug=problem.slug)
    else:
        form = AddNotateForm(request.POST or None, request.FILES or None)

        context = {
            'add_notate': form,
        }
    return render(request, 'problem/add_notate.html', context)


def delete_problem(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)
    problem.delete()
    return redirect('my_problems')


def delete_solution(requets, solution_id):
    solution = Solution.objects.get(pk=solution_id)
    problem = solution.problem.slug
    solution.delete()
    return redirect('detail_problem', slug=problem)


def delete_notate(request, notate_id):
    notate = Notate.objects.get(pk=notate_id)
    problem = notate.problem.slug
    notate.delete()
    return redirect('detail_problem', slug=problem)
