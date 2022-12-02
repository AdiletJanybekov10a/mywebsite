from django.db import models

class Articles(models.Model):
    title = models.CharField('Title', max_length=50)
    anons = models.CharField('Announcement', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date of publication')

    def __str__(self):
        return self.title
        
