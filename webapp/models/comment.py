from django.contrib.auth import get_user_model
from django.db import models
class Comment(models.Model):
    topic = models.ForeignKey('webapp.Topic', on_delete=models.CASCADE, related_name='comments', verbose_name='Topic')
    user = models.ForeignKey(
        get_user_model(),
        related_name="comments",
        on_delete=models.SET_DEFAULT,
        default=1
    )
    text = models.TextField(max_length=400, verbose_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text[:20]}'

    class Meta:
        db_table = "comments"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

