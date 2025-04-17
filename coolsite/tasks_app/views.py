from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView

from tasks_app_user.models import Articles
from django.views.decorators.cache import cache_page



# class TopUsersViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Profile.objects.annotate(avg_rating=Avg('comment__stars')).order_by('-avg_rating')
#     serializer_class = ProfileSerializer

# @method_decorator(cache_page(60 * 15), name='dispatch')
class HomeViews(ListView):
    model = Articles
    template_name = "tasks_app/index.html"
    context_object_name = 'tasks'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            queryset = self.get_queryset().filter(title__icontains=query)
            queryset_price = self.get_queryset().filter(prise__icontains=query)
            if queryset.exists():
                return redirect(f'tasks/{queryset.first().pk}')
            if queryset_price.exists():
                return redirect(f'tasks/{queryset_price.first().pk}')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset()


# def index(request):
#     return render(request, 'tasks_app/index.html')

@method_decorator(cache_page(60 * 15), name='dispatch')
class ViewsAbout(ListView):
    template_name = "tasks_app/about.html"
    queryset = ""
    # def about(self, reqeust):
    #     return render(reqeust, 'tasks_app/about.html')


class ServiceWorkerView(TemplateView):
    template_name = 'serviceworker.js'
    content_type = 'application/javascript'
    name = 'serviceworker.js'
