from django.db import models
import datetime
from django.utils import timezone

class Article(models.Model):
     #Поле для небольшого текста
     #1 аргумент - название, не обязательный
     #2 аргумент - длина текста, обязательный для этого типа
     article_title = models.CharField('название статьи', max_length=200)
     article_text = models.TextField('текст статьи')
     pub_date = models.DateTimeField('дата публикации')

     def __str__(self):
          return self.article_title

     def was_published_recently(self):
          return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

     class Meta:
          verbose_name = 'Статья'
          verbose_name_plural = 'Статьи'

#Комментарии работа с бд
class Cpmment(models.Model):
     #Во время удаления статьи будут удалены все ее коментарии
     article = models.ForeignKey(Article, on_delete=models.CASCADE)
     author_name = models.CharField('автор коментария', max_length= 50)
     comment_text = models.CharField('текст коментария', max_length=200)

     def __str__(self):
          return self.author_name
     
     class Meta:
          verbose_name = 'Комментарий'
          verbose_name_plural = 'Комментарии'
