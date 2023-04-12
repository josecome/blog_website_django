from django.db import models
from blog.models import blogUsers

# Create your models here.
class Posts(models.Model):
    LIST_OF_TYPE_POST = (
        ('Private', 'Private'),
        ('Public', 'Public')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    post_content = models.TextField()   
    post_type = models.CharField(max_length=40, choices=LIST_OF_TYPE_POST)      
    date_created = models.DateField()
    date_updated = models.DateField(null=True)
    link = models.CharField(max_length=100)  
    user_id = models.ForeignKey(blogUsers, on_delete=models.CASCADE)   

    class Meta:  
        db_table = "post"        


class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    type_of_like = models.CharField(max_length=120)
    post_liked_link = models.CharField(max_length=80)   
    date_created = models.DateField()
    date_updated = models.DateField(null=True)
    user_id = models.ForeignKey(Posts, on_delete=models.CASCADE)

    class Meta:  
        db_table = "likes"        


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    post_commented_link = models.CharField(max_length=80)   
    date_created = models.DateField()
    date_updated = models.DateField(null=True)
    user_id = models.ForeignKey(Posts, on_delete=models.CASCADE) 

    class Meta:  
        db_table = "comments"     


class Shares(models.Model):
    id = models.AutoField(primary_key=True)
    post_shared_link = models.CharField(max_length=80)   
    date_created = models.DateField()
    date_updated = models.DateField(null=True)
    user_id = models.ForeignKey(Posts, on_delete=models.CASCADE)

    class Meta:  
        db_table = "contents"       