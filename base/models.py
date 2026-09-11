from django.db import models

class Genre(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    rating=models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    type = models.ForeignKey(Genre, on_delete=models.CASCADE , blank=True, null=True)
    title = models.CharField(max_length=200)
    summary = models.TextField()
    author_name = models.CharField(max_length=100)
    tags = models.CharField(max_length=150)
    image = models.ImageField(upload_to='sakshi_photos',blank=True, null=True )
    video = models.FileField(upload_to='sakshi_videos',blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True,blank=True,null=True) 

    def __str__(self):
        return self.title

