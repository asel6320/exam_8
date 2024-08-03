from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Topic


def title_validate(title):
    if len(title) < 5:
        raise ValidationError("error")


class TopicForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True, label="Title", validators=[title_validate])

    class Meta:
        model = Topic
        fields = ("title", "description")