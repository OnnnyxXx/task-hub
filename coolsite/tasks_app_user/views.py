from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page

from .forms import ArticlesForm
from user_profile.forms import Profile
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count
from .models import *


# @method_decorator(cache_page(60 * 15), name='dispatch')
class TaskView(ListView):
    model = Articles
    template_name = "tasks_app_user/tasks_home.html"
    context_object_name = "tasks_all"

    def get(self, request, *args, **kwargs):
        category = request.GET.get('category')  # Получаем категорию из параметра запроса

        unique_cities = Profile.objects.values_list('city', flat=True).distinct()

        if category:
            tasks_all = Articles.objects.filter(category__name=category).order_by('-data')
        else:
            tasks_all = Articles.objects.order_by('-data')

        unique_cities = [city for city in unique_cities if city is not None]
        categories = Category.objects.all()

        context = {
            'tasks_all': tasks_all,
            'unique_cities': unique_cities,
            'categories': categories,
        }
        return render(request, self.template_name, context)


class CategoryView(ListView):
    model = Category
    template_name = "tasks_app_user/category.html"
    context_object_name = 'categories'  # Имя контекста для списка категорий

    def get_queryset(self):
        return Category.objects.annotate(task_count=Count('articles'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks_all"] = Articles.objects.order_by("-data")
        return context


@method_decorator(login_required, name='dispatch')
class TasksUpdateView(UpdateView):
    model = Articles
    template_name = 'tasks_app_user/create.html'
    form_class = ArticlesForm

    def dispatch(self, request, *args, **kwargs):
        article = self.get_object()

        if article.author != self.request.user:
            return redirect("category")

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        article = form.save(commit=False)
        article.category = form.cleaned_data['category']
        article.save()
        return redirect('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


# DeleteTasks
@method_decorator(login_required, name='dispatch')
class TasksDeleteView(DeleteView):
    model = Articles
    success_url = reverse_lazy('category')
    template_name = 'tasks_app_user/delete_tasks.html'

    def dispatch(self, request, *args, **kwargs):
        Articles = self.get_object()

        if Articles.author != self.request.user:
            return redirect("category")

        return super().dispatch(request, *args, **kwargs)


@method_decorator(cache_page(10), name='dispatch')
class TasksDetailView(DetailView):
    model = Articles
    template_name = 'tasks_app_user/details_tasks.html'
    context_object_name = 'article'


class CreateTask(CreateView):
    model = Articles
    template_name = "tasks_app_user/create.html"
    form_class = ArticlesForm
    success_url = reverse_lazy('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data()
        context['error'] = 'Форма была неверной'
        return self.render_to_response(context)
