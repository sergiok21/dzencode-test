from django.urls import path, include

from comments.views import CommentCreateView


app_name = 'comments'

urlpatterns = [
    path('<int:page>/', CommentCreateView.as_view(), name='paginator'),
]
