from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Project(models.Model):
	"""docstring for Project"""

	name 							= models.CharField(max_length=256, blank=False)
	description						= models.TextField(max_length=4096)

	def __str__(self):
		return self.name


class Exprecord(models.Model):
	"""docstring for Expense record"""

	item 							= models.CharField(max_length=1024, blank=False)
	project							= models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
	date							= models.DateField()
	contributor 					= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	cost 							= models.PositiveIntegerField(default=0)
	proof							= models.FileField(upload_to='proofs/', blank=True)


	def __str__(self):
		return self.item

	
	# ImproperlyConfigured at /post/new/
	# No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
	# after creating a post the PostCreateView doesn't know where to redirect
	def get_absolute_url(self):
		# not using redirect because it will redirect to a specific route whereas
		# reverse returns the full url for the route as a string
		# return reverse('exprecord-detail', kwargs={'pk': self.pk})
		return reverse('exprecord-create')
