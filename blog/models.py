from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,'Draft'),
    (1,'Publish')
)


class Accounts(models.Model):
    name = models.CharField(max_length=50,unique=False)
    username = models.CharField(max_length=50,unique=True)
    email = models.CharField(max_length=50,unique=True)
    bio = models.CharField(max_length=150)
    account_status = models.BooleanField(default=False)
    photo = models.CharField(max_length=300,default='default/login-icon-3048.png')
    password = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self) -> str:
        
        return self.username + ' ' + self.name

class Post(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS,default=0)
    likes = models.ForeignKey(Accounts,on_delete=models.CASCADE,related_name='liked_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=125)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created_on']
        
    def __str__(self) -> str:
        return 'Comment {} by '.format(self.body,self.name)
    