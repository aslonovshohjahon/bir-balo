from django.db import models
from django.utils import timezone



class Category(models.Model):
    title = models.CharField('Nomi', max_length=225)
    date = models.DateTimeField('sana', default = timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'kategoriya'
        verbose_name_plural = 'kategoriyalar'

class Post(models.Model):
    title = models.CharField('Nomi', max_length=225)
    image = models.ImageField('Rasm', blank=True, null=True)
    content = models.TextField('haqida')
    pro = models.IntegerField('ko\'rilganlar', default=0)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField('sana', default=timezone.now)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Yangilik'
        verbose_name_plural = 'Yangiliklar'

class Comment(models.Model):  
    post = models.ForeignKey(Post, on_delete = models.CASCADE)     
    user = models.CharField('foydalanuvchi', max_length = 50)
    text = models. TextField('Komentariya', max_length=1000, null=True)
    date = models.DateTimeField('Sana', default=timezone.now)

    class Meta:
        verbose_name = 'komentariya'
        verbose_name_plural = 'kommentariyalar'