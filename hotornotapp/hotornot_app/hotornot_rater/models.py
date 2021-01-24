from django.db import models

class User(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	first_name = models.CharField(default='', max_length=30)
	last_name = models.CharField(default='', max_length=30)

	def __str__(self):
		return self.username

class Images(models.Model):
	city = models.CharField(max_length=200, default="")
	country = models.CharField(max_length=200, default="")
	imageUploaded = models.ImageField(null=True, blank=True)
	isHot = models.IntegerField(default=0)
	isNot = models.IntegerField(default=0)
	image_user = models.ForeignKey(User, default=0, on_delete=models.CASCADE)  # what did models.CASCADE do again?

	def __str__(self):
		return self.id