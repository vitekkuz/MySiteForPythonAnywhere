import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=200)
    text = models.TextField('Текст статьи')
    created_data = models.DateTimeField('Дата публикации', default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    # def was_published_recently(self):
    #     return self.created_data >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'