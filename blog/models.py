from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=300)
	date = models.DateTimeField()
	tetx = models.TextField()
	imadge = models.ImageField(upload_to='event_image/')
