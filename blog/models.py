from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class Comment(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	post_id = models.ForeignKey('Post')
	comment = models.TextField()
	comment_date = models.DateTimeField(default= timezone.now)

	def __str__(self):
		return self.comment[:20]
