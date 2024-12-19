from django.db import models
from authUser.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title