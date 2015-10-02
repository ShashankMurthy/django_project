from django.db import models
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField(max_length = 200)
    aurthor = models.CharField(max_length = 200)
    date = models.DateTimeField()
    category = models.CharField(max_length = 140)
    body = models.TextField()
    image = models.ImageField('Label', upload_to='static/upload')

    def __unicode__(self):
        return self.title
		

