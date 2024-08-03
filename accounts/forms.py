from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from accounts.models import Profile


class MyUserCreationForm(UserCreationForm):
    avatar = forms.ImageField(required=False)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            avatar = self.cleaned_data.get('avatar')
            Profile.objects.create(user=user, avatar=avatar)
        return user

def file_size(value):  # add this to some file where you can import it from
    limit = 300
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')