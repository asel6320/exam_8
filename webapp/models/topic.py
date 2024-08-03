from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
class Topic(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name='topics',
        verbose_name='user',
        on_delete=models.SET_DEFAULT,
        default=1
    )


    title = models.CharField(blank=True, null=True, max_length=100, verbose_name='Title')
    description = models.TextField(blank=True, null=True, max_length=255, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True)
    reply_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.pk}. {self.title}"

    def get_absolute_url(self):
        return reverse("webapp:topics")

    class Meta:
        db_table = "topics"
        verbose_name = "Topic"
        verbose_name_plural = "Topics"