from django.db import models
from django.utils import timezone # notes current date and time
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # it is going to connect each author to an actual user ie a super user on the website
    title = models.CharField(max_length=70)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now) # current date and time is set as create_date
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        # initially, the published date is null is the post is not published.
        # this method changes the value of published_date to the time when the post is actually published.
    
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})
        # after you're done creating the post and publishing it, the user is taken to the post_detail page
        # where the primary key of the post you just published matches the one shown on the webpage.

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey('blogapp.Post', related_name='comments', on_delete=models.CASCADE)
    # it is a foreign key that comes from bloagapp.Post
    # it is going to connect each comment to an actual post
    author = models.CharField(max_length=30)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text


    