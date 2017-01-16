import uuid


from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Blog(models.Model):
    """
    Model representing the blog post
    """
    title = models.CharField(max_length=200, help_text='Enter blog title')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        """
        String representing a model instance
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of blog model
        """
        return reverse('blog-detail', args=[str(self.id)])


class Author(models.Model):
    """
    Model representing biographical information about the author
    """
    name = models.CharField(
        max_length=200,
        help_text='Enter name of blog author')
    bio = models.TextField(help_text="Enter some of author's biography")

    def __str__(self):
        """
        String representation of an author's instance
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of an author
        """
        return reverse('author-detail', args=[str(self.id)])


class comment(models.Model):
    """
    Model representing comments posted by user
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='Unique ID for this particular comment')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey('Blog', on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String representing a comment
        """
        return "{0}, {1}".format(self.id, self.blog.title)
