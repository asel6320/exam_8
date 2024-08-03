from urllib import request

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import TopicForm, SearchForm
from webapp.models import Topic


class TopicListView(ListView):
    model = Topic
    template_name = "topics/index.html"
    ordering = ['-created_at']
    context_object_name = "topics"
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        print(request.user.is_authenticated, "is_authenticated")
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            return form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(title__contains=self.search_value) | Q(user__contains=self.search_value)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        print("Context data:", context)
        return context


class CreateTopicView(LoginRequiredMixin, CreateView):
    template_name = "topics/create_topic.html"
    form_class = TopicForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TopicDetailView(DetailView):
    template_name = "topics/topic_detail.html"
    model = Topic
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments_list = self.object.comments.order_by("-created_at")

        # Paginate comments
        paginator = Paginator(comments_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        comments = paginator.get_page(page_number)

        context["comments"] = comments
        context["is_paginated"] = comments.has_other_pages()

        return context