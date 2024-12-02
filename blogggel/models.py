from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    # Basic information
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    #content
    article = models.TextField()
    # Metadata
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | Last Updated on {self.updated_on}"

    
class Comment(models.Model):
    # Basic information
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    #content
    body = models.TextField()
    # Metadata
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} | by {self.author}"


class Testimonial(models.Model):
    # Basic information
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="testimonial_name"
    )
    job_title = models.CharField(max_length=200, blank=True, null=True)
    
    #content
    text = models.TextField()
    
    # Metadata
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']  # Newest testimonials first

    def __str__(self):
        return f"{self.name} - {self.job_title if self.job_title else 'Testimonial'}"