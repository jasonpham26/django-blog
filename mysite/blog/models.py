from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approve_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
