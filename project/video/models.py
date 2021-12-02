from django.db import models

class Video(models.Model):
    title = models.CharField('Название', max_length=128)
    desc = models.TextField('Описание', null=True, blank=True)
    url = models.URLField('URL')
    registered_in = models.DateTimeField('Создано', auto_now_add=True)

    def __str__(self):
        return self.title
