from django.db import models
from user.models import User

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)
    image_url=models.URLField()
    content=models.TextField(max_length=1000)

    class Meta:
        db_table='post'
