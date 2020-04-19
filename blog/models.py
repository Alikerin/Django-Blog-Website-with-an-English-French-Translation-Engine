# @Author: Ibrahim Salihu Yusuf <yusuf>
# @Date:   2020-03-20T14:23:12+02:00
# @Email:  sibrahim1396@gmail.com
# @Last modified by:   yusuf
# @Last modified time: 2020-03-25T17:43:03+02:00



from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"), (2, "Unpublished"))
PROJECT_STATUS = ((0, "Ongoing"), (1, "Completed"))
LANGUAGE_CHOICES = [
    ('EN', 'English'),
    ('FR', 'French'),
    ('AR', 'Arabic'),
]

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("post_detail", kwargs={"slug": str(self.slug)})

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Project(models.Model):
    title = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='projects')
    description = models.TextField()
    status = models.IntegerField(choices=PROJECT_STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return str(self.title)

class UserInput(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='user_inputs')
    created_on = models.DateTimeField(auto_now_add=True)
    input = models.TextField()
    output = models.TextField()
    target_language = models.CharField(max_length=2, choices = LANGUAGE_CHOICES, default="EN")

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return str(self.input.split(" ")[:5])
        
