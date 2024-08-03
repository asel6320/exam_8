from django.urls import path
from django.views.generic import RedirectView

from webapp.views import TopicListView, CreateTopicView

app_name = 'webapp'

urlpatterns = [
    path('topics/', TopicListView.as_view(), name='topics'),
    path('', RedirectView.as_view(pattern_name='webapp:topics')),
    path('create/', CreateTopicView.as_view(), name='create_topic'),
]