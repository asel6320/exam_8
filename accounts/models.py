from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='User')
    avatar = models.ImageField(null=True, blank=True, upload_to='avatars', verbose_name='Avatar')
    bio = models.TextField(blank=True, null=True, verbose_name='Bio')
    post_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Role(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name