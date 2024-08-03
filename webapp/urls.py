from django.urls import path
from django.views.generic import RedirectView

from webapp.views import TopicListView, CreateTopicView, TopicDetailView, CreateCommentView, UpdateCommentView, \
    DeleteCommentView

app_name = 'webapp'

urlpatterns = [
    path('topics/', TopicListView.as_view(), name='topics'),
    path('', RedirectView.as_view(pattern_name='webapp:topics')),
    path('create/', CreateTopicView.as_view(), name='create_topic'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('topic/<int:pk>/comment/create/', CreateCommentView.as_view(), name='create_comment'),
    path('comment/<int:pk>/update/', UpdateCommentView.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/', DeleteCommentView.as_view(), name='delete_comment'),
]