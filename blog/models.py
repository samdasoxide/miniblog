import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    """
    Model representing a blog
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        """
        String representing the model object
        """
        return self.name

    def get_abosolute_url(self):
        """
        Returns the url to access a particular blog instance
        """
        return reverse('blog-detail', args=[str(self.id)])


class Author(models.Model):
    """
    Model representing blogger the person creating the blog
    """
    name = models.CharField(max_length=200, help_text='Name of the blogger')
    bio = models.TextField(
        help_text='Biographical information about the blogger')

    def __str__(self):
        """
        String representation of the model object
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance
        """
        return reverse('author', args=[str(self.id)])


class Comment(models.Model):
    """
    Model representing a comment
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(help_text='Share your thoughts')
    post_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        """
        String representation of the model object
        """
        return "{0} ({1})".format(self.id, self.blog.title)
