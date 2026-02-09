from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    followed_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # Users who follow this user
        related_name='followed_by',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        # Users who are followed by this user
        related_name='following',
    )

    def __str__(self):
        return f"{self.followed_by.id} follows {self.following.id}"

    class Meta:
        unique_together = ('followed_by', 'following')
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if self.followed_by == self.following:
            raise ValueError("Users cannot follow themselves.")
        super().save(*args, **kwargs)
