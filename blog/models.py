from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
	CATEGORY = [
	('FAMILY_RELATIONSHIPS', 'Family Relationships'),
	('ROMANTIC_RELATIONSHIPS', 'Romantic Relationships'),
	('WORKPLACE_RELATIONSHIPS', 'Workplace Relationships'),
	('COMMUNNITY_RELATIONSHIPS', 'Community Relationships'),
	# ('COMPLICATED_RELATIONSHIPS', 'Complicated Relationships'),
	# ('SACRED_RELATIONSHIPS', 'Sacred Relationships'),
	# ('FORBIDDEN_RELATIONSHIPS', 'Forbidden Relationships'),
	# ('EXTENDED_RELATIONSHIPS', 'Extended Relationships'),
	# ('FRIENDS_RELATIONSHIPS', 'Friends Relationships'),
	# ('OTHER_RELATIONSHIPS', 'Other Relationships'),
	]

	author = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
	title = models.CharField(max_length=250)
	short_desc = models.CharField(max_length=250, blank=True, null=True)
	category = models.CharField(max_length=100, choices=CATEGORY, default='FAMILY_RELATIONSHIPS', blank=True, null=True)
	blog_image = models.ImageField(upload_to="Media/blog")
	blog_content = models.TextField()
	date_published = models.DateTimeField()
	slug = models.SlugField(null=False, unique=True)


	class Meta:
		verbose_name_plural = 'Blog Posts'

	def __str__(self):
		return self.title
	

	def save(self):
		self.slug = slugify(self.title)
		super(Blog, self).save()

	def get_absolute_url(self):
		return reverse('blog_detail', kwargs={'slug':self.slug})

class Comment(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments')
	user = models.CharField(max_length=80)
	# email = models.EmailField()
	comment_content = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
	approved_comment = models.BooleanField(default=False)

	class Meta:
		ordering = ['date_created']
		verbose_name_plural = 'Comments'

	def approve(self):
		self.approved_comment = True
		self.save()

	def __str__(self):
		return 'Comment {} by {}'.format(self.comment_content, self.author)
