from django.db import models

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=64,verbose_name='Заголовок')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Список'
        verbose_name = 'Список'

class TakeImage(models.Model):
    image = models.ImageField(upload_to='uploads')
    
    def __str__(self):
        return self.image.url