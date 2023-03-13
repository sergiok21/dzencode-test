from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, ListView

from comments.forms import CommentForm
from comments.models import Comments
from common.views import TitleMixin


class CommentCreateView(TitleMixin, CreateView, ListView):
    model = Comments
    template_name = 'comments/index.html'
    form_class = CommentForm
    paginate_by = 25
    title = 'dZENcode'

    def post(self, request, *args, **kwargs):
        form = CommentForm(data=request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            home_page = request.POST.get('home_page')
            parent_comment = request.POST.get('parent_comment') if request.POST.get('parent_comment') else None

            comment = Comments.objects.create(
                name=name, email=email, message=message,
                home_page=home_page, parent_comment=parent_comment
            )
            comment.save()
        return HttpResponseRedirect(reverse('comments:paginator', args=[1]))

    def get_context_data(self, **kwargs):
        context = super(CommentCreateView, self).get_context_data(**kwargs)
        comments = cache.get('comments')
        if not comments:
            context['comments'] = Comments.objects.all()
            cache.set('comments', context['comments'], 30)
        else:
            context['comments'] = comments
        return context
