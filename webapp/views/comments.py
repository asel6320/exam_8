from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import CommentForm
from webapp.models import Topic, Comment


class CreateCommentView(LoginRequiredMixin, CreateView):
    template_name = "comments/create_comment.html"
    form_class = CommentForm

    def form_valid(self, form):
        topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.topic = topic
        comment.user = self.request.user
        comment.save()
        return redirect(topic.get_absolute_url())


class UpdateCommentView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = "comments/update_comment.html"
    form_class = CommentForm
    model = Comment
    permission_required = "webapp.update_comment"

    def has_permission(self):
        # return self.request.user.groups.filter(name="moderators").exists()
        return super().has_permission() or self.request.user == self.get_object().user

    def get_success_url(self):
        return reverse("webapp:topic_detail", kwargs={"pk": self.object.topic.pk})


class DeleteCommentView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Comment
    permission_required = "webapp.delete_comment"
    template_name = "comments/confirm_delete.html"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().user

    def post(self, request, *args, **kwargs):
        self.object = get_object_or_404(Comment, pk=kwargs['pk'])
        topic_pk = self.object.topic.pk
        self.object.delete()
        return redirect(reverse("webapp:topic_detail", kwargs={"pk": topic_pk}))

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)